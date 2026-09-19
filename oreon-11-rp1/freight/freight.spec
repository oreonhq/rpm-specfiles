%global source0_hash b16b4a5c91bfa31cd82412a74cfac4f94745acf88d65093696c9650152110a13

Name:    freight
Version: 0.3.13
Release: 13%{?dist}
Summary: A modern take on the Debian archive

# Automatically converted from old format: BSD - review is highly recommended.
License: LicenseRef-Callaway-BSD
URL:     https://github.com/freight-team/%{name}
Source0: https://github.com/freight-team/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

#Patch needed to set paths referenced in scripts to /usr/share to conform to Fedora standard paths
Patch1:  freight-0.3.13-libs-usrshare.patch

BuildArch: noarch

BuildRequires: make

Requires: coreutils
Requires: dpkg
Requires: gnupg

%description
freight programs create the files needed to serve a Debian archive. The actual
serving is done via your favorite HTTP server.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{version}
%patch -P1 -p1

%build
%make_build

%install
%make_install \
             prefix=%{_prefix} \
             bindir=%{_bindir} \
             libdir=%{_datadir} \
             sysconfdir=%{_sysconfdir} \
             mandir=%{_mandir}

mv %{buildroot}%{_sysconfdir}/%{name}.conf{.example,}

# VARLIB, freight library
mkdir -p %{buildroot}%{_sharedstatedir}/%{name}

# VARCACHE, freight cache (to be served by httpd)
mkdir -p %{buildroot}%{_localstatedir}/cache/%{name}

# some empty config files are shipped
find %{buildroot}%{_sysconfdir} -type f -size 0 -delete

%files
%{_bindir}/%{name}*
%{_datadir}/%{name}
%{_localstatedir}/cache/%{name}
%{_sharedstatedir}/%{name}
%config(noreplace) %{_sysconfdir}/%{name}.conf
%doc %{_mandir}/man1/*
%doc %{_mandir}/man5/*
%doc NOTES README.md
%license LICENSE

%changelog
%autochangelog
