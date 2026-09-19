%global source0_hash cba8f7cd6f77adadf75e5ad39944e7490a00e5ae9a00cd2214119cb338c5abad

Name:           libpgf
Version:        7.21.7
Release:        9%{?dist}
Summary:        PGF (Progressive Graphics File) library

# Automatically converted from old format: LGPLv2+ - review is highly recommended.
License:        LicenseRef-Callaway-LGPLv2+
URL:            http://www.libpgf.org
Source0:        https://downloads.sourceforge.net/project/%{name}/%{name}/%{version}/libpgf.zip

BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  libtool
BuildRequires: make

%description
libPGF contains an implementation of the Progressive Graphics File (PGF)
which is a new image file format, that is based on a discrete, fast
wavelet transform with progressive coding features. PGF can be used
for lossless and lossy compression.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{name}

mv README.txt README

# Fix line endings
sed -i -e 's/\r//' configure.ac Makefile.am src/Makefile.am autogen.sh README

sed -i 's|$(DESTDIR)$(datadir)/doc/$(DOC_MODULE)|$(RPM_BUILD_DIR)/libpgf|g' doc/Makefile.am

sh autogen.sh

%build
# FIXME/TODO: document need for -DLIBPGF_DISABLE_OPENMP
# commit 52c998909401f404f1c7029b537ec900f3f780d0 doesn't say why, but
# I *think* it's related to digikam -- rex
export CFLAGS="%{optflags} -DLIBPGF_DISABLE_OPENMP"
export CXXFLAGS="%{optflags} -DLIBPGF_DISABLE_OPENMP -std=c++14"

%configure --disable-static

%make_build

%install
%make_install

%ldconfig_scriptlets

%files
%doc README
%license COPYING
%{_libdir}/libpgf.so.7*

%files devel
%doc html
%{_includedir}/libpgf/
%{_libdir}/libpgf.so
%{_libdir}/pkgconfig/libpgf.pc
%{_mandir}/man3/*.3*

%changelog
%autochangelog
