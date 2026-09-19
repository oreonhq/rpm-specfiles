%global source0_hash 8c864cc53b00510973b0472bad37b59fcf1b7152558753c84860eb8d53fd79f4

Summary:		Automated Password Generator for random password generation
Name:			apg
Version:		2.3.0b
Release:		52%{?dist}
License:		BSD-3-Clause
URL:			http://www.adel.nursat.kz/%{name}/

# Unpacked tarball, fixed permissions (chmod 755 all dirs) and reuploaded
Source0:		http://www.adel.nursat.kz/%{name}/download/%{name}-%{version}.tar.gz
Source1:		apg.socket
Source2:		apg@.service
Patch0:			apg-2.3.0b-gen_rand_pass.patch
Patch1:                 apg-2.3.0b-null-crypt.patch

BuildRequires: systemd-units
BuildRequires: gcc
BuildRequires: make
BuildRequires: libxcrypt-devel
Requires(post): grep
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units

%description
APG (Automated Password Generator) is the tool set for random password
generation. This standalone version generates some random words of
required type and prints them to standard output.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q

%patch -P 0 -p1 -b .gen_rand_pass
%patch -P 1 -p1

%build
# Build server
make CFLAGS="$RPM_OPT_FLAGS" FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} cliserv

# Build standalone files
make CFLAGS="$RPM_OPT_FLAGS" FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} standalone

%install
install -D apg %{buildroot}%{_bindir}/apg
install -D apgbfm %{buildroot}%{_bindir}/apgbfm
install -D apgd %{buildroot}%{_sbindir}/apgd
install -D -m 644 doc/man/apg.1 %{buildroot}%{_mandir}/man1/apg.1
install -D -m 644 doc/man/apgbfm.1 %{buildroot}%{_mandir}/man1/apgbfm.1
install -D -m 644 doc/man/apgd.8 %{buildroot}%{_mandir}/man8/apgd.8
install -d -m 755 %{buildroot}%{_unitdir}

install -p -m 644 %{SOURCE1} %{buildroot}%{_unitdir}/%{name}.socket
install -p -m 644 %{SOURCE2} %{buildroot}%{_unitdir}/%{name}@.service

%post
# add a service for apg if it doesn't already exist
/bin/grep ^pwdgen /etc/services >& /dev/null
if [ $? == 1 ]; then
    echo -e 'pwdgen\t\t129/tcp\t\t\t# PWDGEN service' >> /etc/services
fi
%if 0%{?fedora} > 17
	%systemd_post apg@.service
%else
if [ $1 -eq 1 ]; then
    # Initial installation
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%endif

%preun
%if 0%{?fedora} > 17
	%systemd_preun apg@.service
%else
if [ $1 -eq 0 ]; then
    # Package removal, not upgrade
    /bin/systemctl --no-reload disable apg@.service > /dev/null 2>&1 || :
    /bin/systemctl stop apg@.service > /dev/null 2>&1 || :
fi
%endif

%postun
%if 0%{?fedora} > 17
	%systemd_postun apg@.service
%else
/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ]; then
    # Package upgrade, not uninstall
    /bin/systemctl try-restart apg@.service >/dev/null 2>&1 || :
fi
%endif

%files
%doc CHANGES COPYING README THANKS TODO doc/rfc*
%{_bindir}/apg
%{_bindir}/apgbfm
%{_sbindir}/apgd
%{_mandir}/man*/*
%{_unitdir}/%{name}@.service
%{_unitdir}/%{name}.socket

%changelog
%autochangelog
