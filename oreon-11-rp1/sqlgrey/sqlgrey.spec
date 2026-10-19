%global source0_hash 94e0fa191b30d672b748e934728ca73383bf9b36e4b17618b01adaaba40280e2
Name:           sqlgrey
Version:        1.8.0
Release:        1%{?dist}
Summary:        Postfix grey-listing policy service
License:        GPL-2.0-or-later
URL:            http://sqlgrey.sourceforge.net/
Source0:        http://dl.sourceforge.net/sqlgrey/sqlgrey-%{version}.tar.gz
Source1:        sqlgrey.service
Patch0:         sqlgrey-1.7.4-sqlite.patch
Patch1:         sqlgrey-1.7.4-warnings.patch
BuildArch:      noarch
Requires:               postfix
Requires:               perl(DBD::SQLite)
Requires(post): systemd
Requires(preun): systemd
Requires(postun): systemd
# oreon:deps
BuildRequires:  make
BuildRequires:  perl-Pod-Perldoc
BuildRequires:  perl-generators
BuildRequires:  perl-podlators
BuildRequires:  systemd
# /oreon:deps
%description
SQLgrey is a Postfix grey-listing policy service with auto-white-listing
written in Perl with SQL database as storage backend.  Greylisting stops 50
to 90% of junk mails (spam and virus) before they reach your Postfix server
(saves BW, user time and CPU time).

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1
%patch -P1 -p1

# Create a sysusers.d config file
cat >sqlgrey.sysusers.conf <<EOF
u sqlgrey - 'SQLgrey server' /var/lib/sqlgrey -
EOF

%build

make %{?_smp_mflags}
%install
rm -rf $RPM_BUILD_ROOT
make rh-install ROOTDIR=$RPM_BUILD_ROOT SBINDIR=$RPM_BUILD_ROOT/usr/bin
install -D -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{_unitdir}/sqlgrey.service
rm -rf $RPM_BUILD_ROOT%{_sysconfdir}/init.d/
mkdir -p -m 755 $RPM_BUILD_ROOT%{_var}/lib
mkdir -m 750 $RPM_BUILD_ROOT%{_var}/lib/sqlgrey
touch $RPM_BUILD_ROOT%{_var}/lib/sqlgrey/sqlgrey.db
install -m0644 -D sqlgrey.sysusers.conf %{buildroot}%{_sysusersdir}/sqlgrey.conf
%oreon_autofiles main

%post

%systemd_post sqlgrey.service
%preun

%systemd_preun sqlgrey.service
%postun

%systemd_postun_with_restart sqlgrey.service
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
