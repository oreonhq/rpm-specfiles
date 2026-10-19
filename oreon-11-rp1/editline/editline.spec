%global source0_hash df223b3333a545fddbc67b49ded3d242c66fadf7a04beb3ada20957fcd1ffc0e
Name:           editline
Version:        1.17.1
Release:        1%{?dist}
Summary:        A small compatible replacement for readline
License:        Spencer-94
URL:            https://troglobit.com/projects/editline/
Source0:        https://github.com/troglobit/editline/releases/download/%{version}/editline-%{version}.tar.xz
Patch0:         https://github.com/troglobit/editline/commit/f53bebdbe98c4dbfc9cc959032a071415324dde2-modified.patch
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
This is a line editing library for UNIX. It can be linked into almost
any program to provide command line editing and history. It is call
compatible with the FSF readline library, but is a fraction of the
size (and offers fewer features).

%package devel
Summary:        Development files for editline
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
Header files for the editline library.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

%configure --disable-static
%make_build
%install
%make_install
rm %{buildroot}/%{_libdir}/libeditline.la
rm %{buildroot}/%{_docdir}/editline/{LICENSE,README.md}
rm %{buildroot}/%{_mandir}/man3/editline.3
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n editline-devel -f %{oreon_filedir}/editline-devel.list

%changelog

%autochangelog
