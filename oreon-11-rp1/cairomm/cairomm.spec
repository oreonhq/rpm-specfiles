%global source2_hash 7d23f51d62fe68e5be48319f151ba31b117f8fea93f2afc5685ed75da64db2f0
%global source1_hash bac7d9a09dbf876aaff86da6f49ffa35465e0cbf0082870a8d534ac4a3598b78
%global source0_hash 70136203540c884e89ce1c9edfb6369b9953937f6cd596d97c78c9758a5d48db
%global so_version 1
%global apiver 1.0
%bcond maintainer_mode 1
Name:           cairomm
Summary:        C++ API for the cairo graphics library
Version:        1.14.5
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
Source0:        https://www.cairographics.org/releases/cairomm-1.14.5.tar.xz
Source1:        https://www.cairographics.org/releases/cairomm-1.14.5.tar.xz.asc
Source2:        https://gitlab.freedesktop.org/freedesktop/freedesktop/uploads/0ac64e9582659f70a719d59fb02cd037/gpg_key.pub
Patch:          https://gitlab.freedesktop.org/cairo/cairomm/-/merge_requests/29.patch
Patch:          https://gitlab.freedesktop.org/cairo/cairomm/-/commit/2b73bbba0f88f1995ce4b1c2a0cf73299bdd654b.patch
Patch:          https://gitlab.freedesktop.org/cairo/cairomm/-/commit/871393804b0bdec39e365a59ceaed7aaee774355.patch
%if %{with maintainer_mode}
%endif
Provides:       cairomm%{apiver}%{?_isa} = %{version}-%{release}
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
BuildRequires:  pkgconfig(sigc++-2.0)
# /oreon:deps
%description
This library provides a C++ interface to cairo.

The API/ABI version series is %{apiver}.

%package        devel
Summary:        Development files for cairomm
Requires:       cairomm%{?_isa} = %{version}-%{release}
Provides:       cairomm%{apiver}-devel%{?_isa} = %{version}-%{release}
%description    devel
The cairomm-devel package contains libraries and header files for developing
applications that use cairomm.

The API/ABI version series is %{apiver}.

%package        doc
Summary:        Documentation for cairomm
License:        %{license} AND MIT
BuildArch:      noarch
Provides:       cairomm%{apiver}-doc = %{version}-%{release}
%{?doxygen_js_requires}
%description    doc
Documentation for cairomm can be viewed through the devhelp documentation
browser.

The API/ABI version series is %{apiver}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} \
    --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'

%autosetup -p1
# Fix stray executable bit:
chmod -v a-x NEWS

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
%oreon_autofiles cairomm-devel usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*
%oreon_autofiles cairomm-doc usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n cairomm-devel -f %{oreon_filedir}/cairomm-devel.list
%files -n cairomm-doc -f %{oreon_filedir}/cairomm-doc.list

%changelog

* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 1.14.5-1
- Prepare for Oreon 11 (RP1)
