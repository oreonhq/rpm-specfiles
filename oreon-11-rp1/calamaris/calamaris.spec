%global source0_hash 62fe534469c28f3335a35ad279c26b22bf6d773306d4f3b438af57d034d3a8ea

%global __requires_exclude ^perl\\(ident\\)$

Summary:        Analyzer and report generator for web proxy servers like Squid
Name:           calamaris
Version:        2.99.4.8
Release:        5%{?dist}
License:        (GPL-1.0-or-later OR Artistic-1.0-Perl) AND GPL-2.0-or-later
URL:            https://cord.de/calamaris-english
Source0:        https://cord.de/files/calamaris/%{name}-%{version}.tar.gz
Patch0:         calamaris-2.99.4.7-use-lib.patch
BuildArch:      noarch
BuildRequires:  perl-generators
Requires:       perl(NetAddr::IP)
# Test in %%check
BuildRequires:  perl-interpreter
BuildRequires:  perl(constant)
BuildRequires:  perl(Carp)
BuildRequires:  perl(File::Path)
BuildRequires:  perl(GD::Graph)
BuildRequires:  perl(GD::Graph::bars)
BuildRequires:  perl(GD::Graph::colour)
BuildRequires:  perl(GD::Graph::utils)
BuildRequires:  perl(Getopt::Long)
BuildRequires:  perl(integer)
BuildRequires:  perl(NetAddr::IP)
BuildRequires:  perl(Socket)
BuildRequires:  perl(strict)
BuildRequires:  perl(Sys::Hostname)
BuildRequires:  perl(Time::Local)

%description
Calamaris is used to produce statistical output from web proxy servers
like Squid, NetCache, Inktomi Traffic Server, Oops! proxy server, Compaq
TaskSmart, Cisco Content Engines, iPlanet Proxy Server or related proxy
log files. The resulting output can be ASCII or HTML with or without
graphics and with or without frames. It is possible to cache calculated
data in a file to use them in later runs.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q
%patch -P0 -p1 -b .use-lib
for file in *.use-lib; do touch -c -r ${file} ${file%.use-lib}; done

%build

%install
install -D -p -m 0755 %{name} $RPM_BUILD_ROOT%{_bindir}/%{name}
install -D -p -m 0644 %{name}.1 $RPM_BUILD_ROOT%{_mandir}/man1/%{name}.1
for file in *.pm; do
  install -D -p -m 0644 ${file} $RPM_BUILD_ROOT%{perl_vendorlib}/%{name}/${file}
done

# Convert files from ISO-8859-1 to UTF-8
for file in CONTRIBUTORS EXAMPLES; do
  iconv -f iso-8859-1 -t utf-8 -o ${file}.utf8 ${file}
  touch -c -r ${file} ${file}.utf8; mv -f ${file}.utf8 ${file}
done

%check
perl -c $RPM_BUILD_ROOT%{_bindir}/%{name}
echo '0 7 192.0.2.42 TCP_HIT/200 4711 GET http://example.net/ - NONE/- text/html' | \
  $RPM_BUILD_ROOT%{_bindir}/%{name}

%files
%license COPYRIGHT
%doc CHANGES CONTRIBUTORS EXAMPLES EXAMPLES.v3 README
%{_bindir}/%{name}
%{perl_vendorlib}/%{name}/
%{_mandir}/man1/%{name}.1*

%changelog
%autochangelog
