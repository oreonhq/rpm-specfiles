%global source0_hash d0365b8b0762a79c3ff7913234099091c365fcae125436343224b4e39da85087
Name:           libjodycode
Version:        4.0.1
Release:        1%{?dist}
Summary:        General purpose utility functions
License:        MIT
URL:            https://codeberg.org/jbruchon/libjodycode/
Source0:        https://codeberg.org/jbruchon/%{name}/archive/%{name}-v%{version}.tar.gz
# oreon:deps
BuildRequires:  gcc
BuildRequires:  make
# /oreon:deps
%description
libjodycode is a software code library containing code shared among
several of the programs written by Jody Bruchon such as imagepile,
jdupes, winregfs, and zeromerge. These shared pieces of code were
copied between each program as they were updated. As the number of
programs increased and keeping these pieces of code synced became more
annoying, the decision was made to combine all of them into a single
reusable shared library.

%package devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir %{name}
%oreon_prep
%build

%make_build HARDEN=1 PREFIX="%{_prefix}" LIB_DIR="%{_libdir}"
%install
%make_install HARDEN=1 PREFIX="%{_prefix}" LIB_DIR="%{_libdir}"
rm -f %{buildroot}%{_libdir}/libjodycode.a
rm -rf %{buildroot}%{_mandir}/man7
%oreon_autofiles main usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/*

%files -f %{oreon_filedir}/main.list
%files -n libjodycode-devel -f %{oreon_filedir}/libjodycode-devel.list

%changelog

%autochangelog
