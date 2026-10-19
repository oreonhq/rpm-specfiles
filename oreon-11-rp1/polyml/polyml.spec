%global source0_hash 5cf5f77767568c25cf880acc2d0a32ee3d399e935475ab1626e8192fc3b07390
%undefine _hardened_build
%global giturl  https://github.com/polyml/polyml
Name:           polyml
Version:        5.9.2
Release:        1%{?dist}
Summary:        Poly/ML compiler and runtime system
License:        LGPL-2.1-or-later
URL:            https://www.polyml.org/
VCS:            git:%{giturl}.git
Source0:        %{giturl}/archive/v%{version}/%{name}-%{version}.tar.gz
ExcludeArch:    %{ix86}
Requires:       gcc-c++
Requires:       polyml-libs%{?_isa} = %{version}-%{release}
# oreon:deps
BuildRequires:  gcc-c++
BuildRequires:  gmp-devel
BuildRequires:  libffi-devel
BuildRequires:  make
# /oreon:deps
%description
Poly/ML is a full implementation of Standard ML available as open-source.
This release supports the ML97 version of the language and the Standard Basis
Library.

%package doc
Summary:        Poly/ML documentation
BuildArch:      noarch
%description doc
Documentation for Poly/ML.

%package libs
Summary:        Poly/ML runtime libraries
%description libs
Runtime libraries for Poly/ML.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%conf
# Fix end of line encoding
sed -i 's/\r//' documentation/main.css

%build

%configure --enable-shared --disable-static \
%ifarch %{x86_64} %{arm64}
  --enable-compact32bit \
%endif
  CPPFLAGS="-D_GNU_SOURCE" \
  CFLAGS="%{build_cflags} -fno-strict-aliasing -Wa,--noexecstack" \
  CXXFLAGS="%{build_cxxflags} -fno-strict-aliasing -Wa,--noexecstack" \
  CCASFLAGS="-Wa,--noexecstack" \
  LDFLAGS="%{build_ldflags} -Wl,-z,noexecstack"
sed -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    -e 's|CC="\(.*g..\)"|CC="\1 -Wl,--as-needed"|' \
    -i libtool
%make_build
extflags=$(sed 's/[[:space:]]*$//' <<< '%{extension_cflags}')
sed -e 's/-Wl,-rpath,\${LIBDIR} //'\
    -e 's/-lffi //;s/-lgmp //' \
    -e "s/^\(CFLAGS=\).*/\1\"-O2 -pipe -fno-strict-aliasing $extflags\"/" \
    -i polyc
%install
%make_install
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

make check
%files -f %{oreon_filedir}/main.list
%files -n polyml-doc -f %{oreon_filedir}/polyml-doc.list
%files -n polyml-libs -f %{oreon_filedir}/polyml-libs.list

%changelog

%autochangelog
