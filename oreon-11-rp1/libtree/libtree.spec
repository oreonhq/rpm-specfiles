%global source0_hash b804e6d1a0ded7ea81724467496cc2b3a003ec5110b7ba36288779aba902fee0
%global debug_package %{nil}
Name:           libtree
Version:        1.0
Release:        12%{?dist}
Summary:        Implementation of AVL (Adelson-Velskii and Landis) balanced trees
License:        MIT
URL:            https://piumarta.com/software/tree/
Source0:        https://piumarta.com/software/tree//tree-%{version}.tar.gz
%define common_desc tree.h Implementation of AVL (Adelson-Velskii and Landis) \
balanced trees in the spirit of the BSD queue and list implementations.
# oreon:deps

# /oreon:deps
%description
%{common_desc}

%package  devel
Summary:  %{summary}
Provides: libtree-static = %{version}-%{release}
%description devel
%{common_desc}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir tree-%{version}
%oreon_prep
%build

%install
mkdir -p %{buildroot}%{_includedir}
install -p -m 644 tree.h %{buildroot}%{_includedir}
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libtree-devel -f %{oreon_filedir}/libtree-devel.list

%changelog

%autochangelog
