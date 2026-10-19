%global source0_hash f95cf60a22d4e461bec9d0e72f5d3609c9a4576fb1cc45f553d0202ce2e38c88
Name:            monotone
Version:         1.1
Release:        1%{?dist}
Summary:        A free, distributed version control system
License:         GPL-2.0-or-later
URL:             http://monotone.ca/
Source0:        http://monotone.ca/downloads/%{version}/%{name}-%{version}.tar.bz2
Source1:         monotone.service
Source2:         monotone.sysconfig
Source3:         README.monotone-server
Source4:         monotone-server-tmpfiles.conf
Source5:         monotone-server-initdb
Source6:         monotone-server-migratedb
Source7:         monotone-server-genkey
Source8:         monotone-server-import
Source9:         monotone-server-sysusers.conf
Patch0:          monotone-1.0-stacktrace-on-crash.patch
Patch1:          monotone-1.1-iostream.patch
Patch2:          monotone-1.1-lua-integer.patch
Patch3:          monotone-1.1-pcre.patch
Patch4:          monotone-1.1-py3.patch
Patch5:          monotone-1.1-lua-ql.patch
Patch6:          monotone-1.1-boost.patch
Patch7:          monotone-1.1-string-overflow.patch
Patch8:          monotone-1.1-catch.patch
%{?sysusers_requires_compat}
%{?perl_default_filter}
# oreon:deps
BuildRequires:  bash-completion
BuildRequires:  boost-devel
BuildRequires:  botan-devel
BuildRequires:  cvs
BuildRequires:  expect
BuildRequires:  gcc-c++
BuildRequires:  libidn-devel
BuildRequires:  lua-devel
BuildRequires:  make
BuildRequires:  pcre-devel
BuildRequires:  perl-generators
BuildRequires:  sqlite-devel
BuildRequires:  systemd
BuildRequires:  systemd-rpm-macros
BuildRequires:  zlib-devel
# /oreon:deps
%description
monotone is a free, distributed version control system.
It provides fully disconnected operation, manages complete
tree versions, keeps its state in a local transactional
database, supports overlapping branches and extensible
metadata, exchanges work over plain network protocols,
performs history-sensitive merging, and delegates trust
functions to client-side RSA certificates.

%package server
Summary: Standalone server setup for monotone
Requires: monotone = %{version}-%{release}
Requires(pre): shadow-utils
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
%description server
This package provides an easy-to-use standalone server setup for monotone.

%package -n perl-Monotone
Summary: Perl Module for monotone
Requires: monotone = %{version}-%{release}
%description -n perl-Monotone
This is a simple Perl module to start a monotone automate sub-process
and then pass commands to it.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
%build

export LC_MESSAGES=en_US
%configure
%make_build
%check

%install
export LC_MESSAGES=en_US
%make_install
rm -f %{buildroot}%{_infodir}/dir
mv %{buildroot}%{_datadir}/doc/%{name} _doc
%find_lang %{name}
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_localstatedir}/lib
ln -snf ../bin/mtn %{buildroot}%{_sbindir}/monotone-server
ln -snf mtn.1 %{buildroot}%{_mandir}/man1/monotone-server.1
install -D -m 0644 -p %{SOURCE1} %{buildroot}%{_unitdir}/monotone.service
install -D -m 0644 -p %{SOURCE2} %{buildroot}%{_sysconfdir}/sysconfig/monotone
install -d -m 0755 %{buildroot}%{_sysconfdir}/monotone
install -d -m 0750 %{buildroot}%{_sysconfdir}/monotone/private-keys
install -d -m 0770 %{buildroot}%{_localstatedir}/lib/monotone
install -d -m 0755 %{buildroot}%{_localstatedir}/run/monotone
install -D -m 0644 %{SOURCE4} \
             %{buildroot}%{_tmpfilesdir}/monotone.conf
install -D -m 0755 -p %{SOURCE5} %{buildroot}%{_libexecdir}/monotone-server-initdb
install -D -m 0755 -p %{SOURCE6} %{buildroot}%{_libexecdir}/monotone-server-migratedb
install -D -m 0755 -p %{SOURCE7} %{buildroot}%{_libexecdir}/monotone-server-genkey
install -D -m 0755 -p %{SOURCE8} %{buildroot}%{_libexecdir}/monotone-server-import
install -m 0440 /dev/null \
             %{buildroot}%{_sysconfdir}/monotone/passphrase.lua
install -m 0640 /dev/null \
             %{buildroot}%{_sysconfdir}/monotone/read-permissions
install -m 0640 /dev/null \
             %{buildroot}%{_sysconfdir}/monotone/write-permissions
install -m 0644 /dev/null \
             %{buildroot}%{_sysconfdir}/monotone/monotonerc
install -m 0640 /dev/null \
             %{buildroot}%{_localstatedir}/lib/monotone/server.mtn
install -m 0644 -p %{SOURCE3} .
install -D -m 0644 -p contrib/Monotone.pm \
             %{buildroot}%{perl_vendorlib}/Monotone.pm
mkdir -p %{buildroot}%{_datadir}/bash-completion/completions
mv %{buildroot}%{_sysconfdir}/bash_completion.d/monotone.bash_completion \
             %{buildroot}%{_datadir}/bash-completion/completions/%{name}.bash_completion
install -p -D -m 0644 %{SOURCE9} %{buildroot}%{_sysusersdir}/monotone-server.conf
%oreon_autofiles perl-Monotone usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/* usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%pre server

%sysusers_create_compat %{SOURCE9}
%post server

%systemd_post monotone.service
%preun server

%systemd_preun monotone.service
%postun server

%systemd_postun monotone.service
%files -f %{oreon_filedir}/main.list
%files -n monotone-server -f %{oreon_filedir}/monotone-server.list
%files -n perl-Monotone -f %{oreon_filedir}/perl-Monotone.list

%changelog

%autochangelog
