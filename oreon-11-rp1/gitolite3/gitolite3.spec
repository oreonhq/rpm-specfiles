%global source0_hash 9c354234446680d3a890c5cf754679541fe6e41419ab02fbf4fe8cc3989a6b33

%global perl_vendorlib %(eval $(perl -V:vendorlib); echo $vendorlib)
# RHEL uses %%{_prefix}/com for %%{_sharedstatedir} instead of /var/lib
%if 0%{?rhel}
%global gitolite_homedir /var/lib/%{name}
%else
%global gitolite_homedir %{_sharedstatedir}/%{name}
%endif

Name:           gitolite3
Epoch:          1
Version:        3.6.15
Release:        1%{?dist}
Summary:        Highly flexible server for git directory version tracker

License:        GPL-2.0-only AND CC-BY-SA-1.0
URL:            http://github.com/sitaramc/gitolite
Source0:        https://github.com/sitaramc/gitolite/archive/v%{version}.tar.gz
Source1:        gitolite3-README-fedora
# Upstream: https://github.com/sitaramc/gitolite/commit/c656af01b73a5cc4f80512
Source2:        compile-1

BuildArch:      noarch
BuildRequires:      perl-generators
Provides:       perl(%{name}) = %{version}-%{release}
Requires:       git
Requires:       openssh-clients
Recommends:       subversion

%description
Gitolite allows a server to host many git repositories and provide access
to many developers, without having to give them real userids on the server.
The essential magic in doing this is ssh's pubkey access and the authorized
keys file, and the inspiration was an older program called gitosis.

Gitolite can restrict who can read from (clone/fetch) or write to (push) a
repository. It can also restrict who can push to what branch or tag, which
is very important in a corporate environment. Gitolite can be installed
without requiring root permissions, and with no additional software than git
itself and perl. It also has several other neat features described below and
elsewhere in the doc/ directory.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn gitolite-%{version}
cp %{SOURCE1} .

# Create a sysusers.d config file
cat >gitolite3.sysusers.conf <<EOF
u gitolite3 - 'git repository hosting' %{gitolite_homedir} /bin/sh
EOF

%build
#This page intentionally left blank.

%install
rm -rf $RPM_BUILD_ROOT

# Directory structure
install -d $RPM_BUILD_ROOT%{gitolite_homedir}
install -d $RPM_BUILD_ROOT%{gitolite_homedir}/.ssh
install -d $RPM_BUILD_ROOT%{_bindir}
install -d $RPM_BUILD_ROOT%{perl_vendorlib}
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}

# Code
cp -pr src/lib/Gitolite $RPM_BUILD_ROOT%{perl_vendorlib}
echo "%{version}-%{release}" >src/VERSION
cp -a src/* $RPM_BUILD_ROOT%{_datadir}/%{name}
cp %{SOURCE2} $RPM_BUILD_ROOT%{_datadir}/%{name}/commands/
ln -s %{_datadir}/%{name}/gitolite $RPM_BUILD_ROOT%{_bindir}/gitolite

# empty authorized_keys file
touch $RPM_BUILD_ROOT%{gitolite_homedir}/.ssh/authorized_keys

install -m0644 -D gitolite3.sysusers.conf %{buildroot}%{_sysusersdir}/gitolite3.conf

%files
%{_bindir}/*
%{perl_vendorlib}/*
%{_datadir}/%{name}
# make homedir non world readable
%attr(750,%{name},%{name}) %dir %{gitolite_homedir}
%attr(750,%{name},%{name}) %dir %{gitolite_homedir}/.ssh
%config(noreplace) %attr(640,%{name},%{name}) %{gitolite_homedir}/.ssh/authorized_keys
%doc gitolite3-README-fedora COPYING README.markdown CHANGELOG
%{_sysusersdir}/gitolite3.conf

%changelog
%autochangelog
