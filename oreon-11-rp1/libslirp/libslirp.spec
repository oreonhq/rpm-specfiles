Name:           libslirp
Version:        4.9.1
Release:        3%{?dist}
Summary:        A general purpose TCP-IP emulator

# check the SPDX tags in source files for details
License:        BSD-3-Clause AND MIT
URL:            https://gitlab.freedesktop.org/slirp/%{name}
Source0:        https://gitlab.freedesktop.org/slirp/libslirp/-/archive/v4.9.1/libslirp-4.9.1.tar.xz
# oreon url source checksums begin
%global source0_sha256 7e607332b2d167663b0a8781113eef7e9115694404a8f576b5527b82ab76d53b
%global source0_file libslirp-4.9.1.tar.xz
# oreon url source checksums end

BuildRequires:  git-core
BuildRequires:  meson
BuildRequires:  gcc
BuildRequires:  glib2-devel

%description
A general purpose TCP-IP emulator used by virtual machine hypervisors
to provide virtual networking services.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
# oreon verify url source checksums begin
%(f=%{_sourcedir}/libslirp-4.9.1.tar.xz; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "7e607332b2d167663b0a8781113eef7e9115694404a8f576b5527b82ab76d53b" || { echo "oreon: Source0 SHA256 mismatch for libslirp-4.9.1.tar.xz" >&2; exit 1; })
# oreon verify url source checksums end
%autosetup -S git_am

%build
%meson
%meson_build


%install
%meson_install


%files
%license COPYRIGHT
%doc README.md CHANGELOG.md
%{_libdir}/%{name}.so.0*

%files devel
%dir %{_includedir}/slirp/
%{_includedir}/slirp/*
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/slirp.pc


%changelog
* Mon May 25 2026 Oreon Packaging Team <packaging@oreonhq.com> - 4.9.1-3
- Import
