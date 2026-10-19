%global source0_hash d10566a2e01eed061363c727565e171b8d9938f76c5ded49b972fba16e54369e
%global srcname switchtec-user
Name:           switchtec
Version:        4.4
Release:        1%{?dist}
Summary:        Userspace code for the Microsemi PCIe switch
License:        MIT
URL:            https://github.com/Microsemi/switchtec-user
Source0:        https://github.com/Microsemi/%{srcname}/archive/v%{version}/%{srcname}-%{version}.tar.gz
Suggests:       bash-completions
# oreon:deps
BuildRequires:  doxygen
BuildRequires:  gcc
BuildRequires:  graphviz
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel
# /oreon:deps
%description
Easy to use CLI and C library for communicating with Microsemi's Switchtec
management interface.

%package        libs
Summary:        Shared Libraries for %{name}
%description    libs
This package contains shared libraries for %{name}.

%package        devel
Summary:        Development headers and libraries for %{name}
Requires:       %{name}-libs%{?_isa} = %{version}-%{release}
%description    devel
This package contains development headers and libraries for %{name}.

%package        doc
Summary:        Documentation for %{name}
BuildArch:      noarch
%description    doc
This package contains additional documentation for %{name}.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

%build

%configure
%make_build
%make_build -C doc
%install
%make_install \
  PREFIX="%{_prefix}" \
  LIBDIR="%{buildroot}%{_libdir}" \
  LDCONFIG=/bin/true
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
rm -r %{buildroot}%{_sysconfdir}
rm %{buildroot}%{_libdir}/*.a
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/include/* usr/*/pkgconfig/* usr/lib*/cmake/* usr/share/aclocal/* usr/*/lib*.so usr/share/cmake/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%files -f %{oreon_filedir}/main.list
%files -n switchtec-libs -f %{oreon_filedir}/switchtec-libs.list
%files -n switchtec-devel -f %{oreon_filedir}/switchtec-devel.list
%files -n switchtec-doc -f %{oreon_filedir}/switchtec-doc.list

%changelog

%autochangelog
