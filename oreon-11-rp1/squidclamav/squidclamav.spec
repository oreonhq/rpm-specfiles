%global source0_hash 93c2c277f5e1fc334afd4794ef35faf0ada6fbd7acdd7085f37618d4eff53c1f

Name:           squidclamav
Version:        7.4
Release:        3%{?dist}
Summary:        HTTP Antivirus for Squid based on ClamAv and the ICAP protocol
License:        GPL-3.0-or-later
URL:            https://squidclamav.darold.net/

Source0:        https://github.com/darold/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf

BuildRequires:  bzip2-devel
BuildRequires:  c-icap-devel
BuildRequires:  gcc
BuildRequires:  libarchive-devel
BuildRequires:  make
BuildRequires:  zlib-devel

Requires:       c-icap
Requires:       squid

%if 0%{?rhel} == 7
Requires:       httpd
%else
Requires:       httpd-filesystem
%endif

%description
SquidClamav is an antivirus for the Squid proxy based on the ICAP protocol and
the awards-winning ClamAv anti-virus toolkit. Using it will help you secure your
home or enterprise network web traffic. SquidClamav is the most efficient
antivirus tool for HTTP traffic available for free, it is written in C as a
c-icap service and can handle several thousands of connections at once.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1

%build
%configure \
  --disable-static \
  --enable-shared \
  --with-c-icap \
  --with-libarchive

%make_build

%install
%make_install
find %{buildroot} -name '*.la' -delete

install -D -m644 %{SOURCE1} %{buildroot}%{_sysconfdir}/httpd/conf.d/%{name}.conf

# Let rpm pick up the docs in the files section
rm -rf %{buildroot}%{_datadir}/%{name}

# Do not add default configuration files
rm -f %{buildroot}%{_sysconfdir}/c-icap/*.default

%files
%license COPYING
%doc AUTHORS ChangeLog README
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/c-icap/%{name}.conf
%config(noreplace) %{_sysconfdir}/httpd/conf.d/%{name}.conf
%{_datadir}/c_icap/templates/squidclamav/
%{_libdir}/c_icap/*.so
%{_libexecdir}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
