%global source2_hash b1457513a743cff02a2d70908b127b1887dae88c9fe62db6299be3c7ccd55e4f
%global source0_hash e0e996a979ee52c840dca3ee74f5d005e3259b94ddce58f255d3b6f47c8cb41d
%global so_version 1
%global apiver 1.16
%bcond maintainer_mode 1
Name:           cairomm%{apiver}
Summary:        C++ API for the cairo graphics library
Version:        1.18.1
Release:        1%{?dist}
URL:            https://www.cairographics.org
License:        LGPL-2.0-or-later
SourceLicense:  %{shrink:
                %{license} AND
                FSFAP AND
                GPL-2.0-or-later AND
                LGPL-2.1-or-later AND
                MIT
                }
%global src_base https://www.cairographics.org/releases
Source0:        %{src_base}/cairomm-%{version}.tar.xz
Source1:        %{src_base}/cairomm-%{version}.tar.xz.asc
Source2:        https://gitlab.freedesktop.org/freedesktop/freedesktop/uploads/0ac64e9582659f70a719d59fb02cd037/gpg_key.pub
%if %{with maintainer_mode}
%endif
# oreon:deps
BuildRequires:  boost-devel
BuildRequires:  doxygen
BuildRequires:  gcc-c++
BuildRequires:  gpgverify
BuildRequires:  graphviz
BuildRequires:  libxslt
BuildRequires:  meson
BuildRequires:  mm-common
BuildRequires:  pkgconfig(cairo)
BuildRequires:  pkgconfig(cairo-ft)
BuildRequires:  pkgconfig(cairo-pdf)
BuildRequires:  pkgconfig(cairo-png)
BuildRequires:  pkgconfig(cairo-ps)
BuildRequires:  pkgconfig(cairo-svg)
BuildRequires:  pkgconfig(cairo-xlib)
BuildRequires:  pkgconfig(cairo-xlib-xrender)
BuildRequires:  pkgconfig(fontconfig)
BuildRequires:  pkgconfig(mm-common-libstdc++)
BuildRequires:  pkgconfig(sigc++-3.0)
# /oreon:deps
%description
This library provides a C++ interface to cairo.

The API/ABI version series is %{apiver}.

%package        devel
Summary:        Development files for cairomm%{apiver}
Requires:       cairomm%{apiver}%{?_isa} = %{version}-%{release}
%description    devel
The cairomm%{apiver}-devel package contains libraries and header files for
developing applications that use cairomm%{apiver}.

The API/ABI version series is %{apiver}.

%package        doc
Summary:        Documentation for cairomm%{apiver}
License:        %{license} AND MIT
BuildArch:      noarch
%{?doxygen_js_requires}
%description    doc
Documentation for cairomm%{apiver} can be viewed through the devhelp
documentation browser.

The API/ABI version series is %{apiver}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} \
    --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -n cairomm-%{version} -p1

# Remove the tag file, which triggers a rebuild of the documentation.
# While we are at it, we might as well rebuild the devhelp XML too.
rm -rf untracked/docs/reference/html
rm untracked/docs/reference/cairomm-%{apiver}.tag \
   untracked/docs/reference/cairomm-%{apiver}.devhelp2

%conf
%meson \
  -Dmaintainer-mode=%{?with_maintainer_mode:true}%{?!with_maintainer_mode:false} \
  -Dbuild-documentation=true \
  -Dbuild-examples=false \
  -Dbuild-tests=true \
  -Dboost-shared=true \
  -Dwarnings=max

%build

%meson_build
%install
%meson_install
install -t %{buildroot}%{_docdir}/cairomm-%{apiver} -m 0644 -p \
    ChangeLog NEWS README.md
cp -rp examples %{buildroot}%{_docdir}/cairomm-%{apiver}/
%{doxygen_unbundle_buildroot}
%oreon_autofiles cairomm1.16-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cairomm1.16-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n cairomm1.16-devel -f %{oreon_filedir}/cairomm1.16-devel.list
%files -n cairomm1.16-doc -f %{oreon_filedir}/cairomm1.16-doc.list

%changelog

%autochangelog
