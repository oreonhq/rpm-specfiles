%global source0_hash 8c864cc53b00510973b0472bad37b59fcf1b7152558753c84860eb8d53fd79f4
Summary:        Automated Password Generator for random password generation
Name:			apg
Version:		2.3.0b
Release:        52%{?dist}
License:		BSD-3-Clause
URL:			http://www.adel.nursat.kz/%{name}/
Source0:        http://www.adel.nursat.kz/%{name}/download/%{name}-%{version}.tar.gz
Source1:		apg.socket
Source2:		apg@.service
Patch0:			apg-2.3.0b-gen_rand_pass.patch
Patch1:                 apg-2.3.0b-null-crypt.patch
Requires(post): grep
Requires(post): systemd-units
Requires(preun): systemd-units
Requires(postun): systemd-units
# oreon:deps
BuildRequires:  gcc
BuildRequires:  libxcrypt-devel
BuildRequires:  make
BuildRequires:  systemd-units
# /oreon:deps
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

make CFLAGS="$RPM_OPT_FLAGS" FLAGS="$RPM_OPT_FLAGS" %{?_smp_mflags} cliserv
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
%oreon_autofiles main

%post

/bin/grep ^pwdgen /etc/services >& /dev/null
if [ $? == 1 ]; then
    echo -e 'pwdgen\t\t129/tcp\t\t\t# PWDGEN service' >> /etc/services
fi
if [ $1 -eq 1 ]; then
    /bin/systemctl daemon-reload >/dev/null 2>&1 || :
fi
%preun

if [ $1 -eq 0 ]; then
    /bin/systemctl --no-reload disable apg@.service > /dev/null 2>&1 || :
    /bin/systemctl stop apg@.service > /dev/null 2>&1 || :
fi
%postun

/bin/systemctl daemon-reload >/dev/null 2>&1 || :
if [ $1 -ge 1 ]; then
    /bin/systemctl try-restart apg@.service >/dev/null 2>&1 || :
fi
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
