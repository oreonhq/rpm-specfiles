%global source2_hash 29c8ffc9ffee2982ad3c3355736ed043377c1f0f4ea4776df4b98a464692b70e
%global source1_hash f42a9bc9eade399a92981c68c73f3a12cc517b49c7bc0976c6aae19727be3520
%global source0_hash e9b6fe3ede984fa53f2edcebdabb35fb99ace807722772156aea49c079cad191
%global         maj 0
Name:           zix
Version:        0.8.0
Release:        1%{?dist}
Summary:        A lightweight C library of portability wrappers and data structures
License:        ISC
URL:            https://gitlab.com/drobilla/%{name}
Source0:        https://download.drobilla.net/%{name}-%{version}.tar.xz
Source1:        https://download.drobilla.net/%{name}-%{version}.tar.xz.sig
Source2:        https://drobilla.net/drobilla.gpg
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  gnupg2
BuildRequires:  meson
BuildRequires:  python3-sphinx
BuildRequires:  python3-sphinxygen
# /oreon:deps
%description
%{name} is a lightweight C library of portability wrappers and data structures.

%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package        doc
Summary:        Documentation files for %{name}
Provides:       bundled(js-jquery) = 3.6.0
Buildarch:      noarch
%description    doc
The %{name}-doc package contains documentation files for
developing applications that use %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%{gpgverify} --keyring='%{SOURCE2}' --signature='%{SOURCE1}' --data='%{SOURCE0}'
%autosetup

%build

%meson -Dbenchmarks=disabled
%meson_build
%install
%meson_install
rm -rf %{buildroot}%{_docdir}/%{name}-%{maj}/singlehtml
rm -f %{buildroot}%{_docdir}/%{name}-%{maj}/html/.buildinfo
install -d %{buildroot}%{_docdir}/%{name}
mv %{buildroot}%{_docdir}/%{name}-%{maj} %{buildroot}%{_docdir}/%{name}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%meson_test
%files -f %{oreon_filedir}/main.list
%files -n zix-devel -f %{oreon_filedir}/zix-devel.list
%files -n zix-doc -f %{oreon_filedir}/zix-doc.list

%changelog

%autochangelog
