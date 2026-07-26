%global source0_hash 55061450215b170dc8aef476670ccf44a01ff0b7584c3d6894f6d97c077ec7fc

%global srcname switchtec-user

Name:           switchtec
Version:        4.3
Release:        %autorelease
Summary:        Userspace code for the Microsemi PCIe switch

License:        MIT
URL:            https://github.com/Microsemi/switchtec-user
Source:         %{url}/archive/v%{version}/%{srcname}-%{version}.tar.gz

BuildRequires:  doxygen
BuildRequires:  graphviz
BuildRequires:  gcc
BuildRequires:  make
BuildRequires:  ncurses-devel
BuildRequires:  openssl-devel

Suggests:       bash-completions

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

# Relocate bash completion config
install -Dpm0644 -t %{buildroot}%{_datadir}/bash-completion/completions \
  %{buildroot}%{_sysconfdir}/bash_completion.d/%{name}
rm -r %{buildroot}%{_sysconfdir}

# We don't want static libraries
rm %{buildroot}%{_libdir}/*.a

%files
%license LICENSE
%doc README.md
%{_bindir}/%{name}
%dir %{_datadir}/bash-completion
%dir %{_datadir}/bash-completion/completions
%{_datadir}/bash-completion/completions/%{name}

%files libs
%license LICENSE
%{_libdir}/lib%{name}.so.4*

%files devel
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so

%files doc
%license LICENSE
%doc doc/doxygen/html

%changelog
%autochangelog
