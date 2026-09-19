%global source0_hash 35e9b8f4fcd4c45783c595b685fde006c25c12e1de858071d520bad22458213c

Name:           digdoc
Version:        0.0.2
Release:        %autorelease
Summary:        A DNS-over-CoAP client

License:        MIT
URL:            https://github.com/dig-doc/digdoc
Source:         %{url}/archive/v%{version}/digdoc-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  libcoap-devel
BuildRequires:  ldns-devel
# Documentation dependencies
BuildRequires:  help2man

%description
digdoc is a lightweight command-line tool written in C that acts as a
DNS-over-CoAP (DoC) client. Since most common DNS servers do not natively
support CoAP, digdoc currently uses the aiodns-proxy project to translate
CoAP packets into standard UDP-based DNS queries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n digdoc-%{version} -p1

%build
%cmake
%cmake_build
# Build documentation
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=digdoc.1 %{_builddir}/digdoc-%{version}/%{__cmake_builddir}/digdoc

%install
%cmake_install
mkdir -p %{buildroot}/%{_mandir}/man1
install digdoc.1 %{buildroot}/%{_mandir}/man1/digdoc.1

%check
# Tests need internet access
# https://github.com/dig-doc/digdoc/issues/4

%files
%license LICENSE
%doc README.md
%{_bindir}/digdoc
%{_mandir}/man1/digdoc.1*

%changelog
%autochangelog
