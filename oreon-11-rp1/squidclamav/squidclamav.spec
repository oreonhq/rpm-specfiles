%global source0_hash 4d076b692e45cb78b384b5c4a1c63f755d565bdc01c732cc5ddbb8b4f046ceae
Name:           squidclamav
Version:        7.5
Release:        1%{?dist}
Summary:        HTTP Antivirus for Squid based on ClamAv and the ICAP protocol
License:        GPL-3.0-or-later
URL:            https://squidclamav.darold.net/
Source0:        https://github.com/darold/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:        %{name}-httpd.conf
Requires:       c-icap
Requires:       squid
Requires:       httpd-filesystem
# oreon:deps
BuildRequires:  bzip2-devel
BuildRequires:  c-icap-devel
BuildRequires:  gcc
BuildRequires:  libarchive-devel
BuildRequires:  make
BuildRequires:  zlib-devel
# /oreon:deps
%description
SquidClamav is an antivirus for the Squid proxy based on the ICAP protocol and
the awards-winning ClamAv anti-virus toolkit. Using it will help you secure your
home or enterprise network web traffic. SquidClamav is the most efficient
antivirus tool for HTTP traffic available for free, it is written in C as a
c-icap service and can handle several thousands of connections at once.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%oreon_prep
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
rm -rf %{buildroot}%{_datadir}/%{name}
rm -f %{buildroot}%{_sysconfdir}/c-icap/*.default
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
