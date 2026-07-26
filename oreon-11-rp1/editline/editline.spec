%global source0_hash df223b3333a545fddbc67b49ded3d242c66fadf7a04beb3ada20957fcd1ffc0e

Name:           editline
Version:        1.17.1
Release:        16%{?dist}
Summary:        A small compatible replacement for readline

# https://fedoraproject.org/wiki/Licensing/Henry_Spencer_Reg-Ex_Library_License
# also cf https://www.openhub.net/licenses/cnews
License:        Spencer-94
URL:            https://troglobit.com/projects/editline/
Source0:        https://github.com/troglobit/editline/releases/download/%{version}/editline-%{version}.tar.xz
Patch0:         https://github.com/troglobit/editline/commit/f53bebdbe98c4dbfc9cc959032a071415324dde2-modified.patch
BuildRequires:  gcc
BuildRequires: make

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

%autosetup -p1

%build
%configure --disable-static
%make_build

%install
%make_install

rm %{buildroot}/%{_libdir}/libeditline.la
rm %{buildroot}/%{_docdir}/editline/{LICENSE,README.md}
rm %{buildroot}/%{_mandir}/man3/editline.3

%files
%license LICENSE
%{_libdir}/libeditline.so.1
%{_libdir}/libeditline.so.1.0.2

%files devel
%doc ChangeLog.md README.md
%{_includedir}/editline.h
%{_libdir}/libeditline.so
%{_libdir}/pkgconfig/libeditline.pc
# conflicts with libedit-devel
#%%{_mandir}/man3/editline.3.gz

%changelog
%autochangelog
