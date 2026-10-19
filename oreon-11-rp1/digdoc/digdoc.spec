%global source0_hash 35e9b8f4fcd4c45783c595b685fde006c25c12e1de858071d520bad22458213c
Name:           digdoc
Version:        0.0.2
Release:        1%{?dist}
Summary:        A DNS-over-CoAP client
License:        MIT
URL:            https://github.com/dig-doc/digdoc
Source0:        https://github.com/dig-doc/%{name}/archive/v%{version}/%{name}-%{version}.tar.gz
# oreon:deps
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  help2man
BuildRequires:  ldns-devel
BuildRequires:  libcoap-devel
# /oreon:deps
%description
digdoc is a lightweight command-line tool written in C that acts as a
DNS-over-CoAP (DoC) client. Since most common DNS servers do not natively
support CoAP, digdoc currently uses the aiodns-proxy project to translate
CoAP packets into standard UDP-based DNS queries.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%global oreon_srcdir digdoc-%{version}
%oreon_prep
%build

%cmake
%cmake_build
help2man --version-string='%{version}' --no-discard-stderr  --no-info --name='%{summary}' --output=digdoc.1 %{_builddir}/digdoc-%{version}/%{__cmake_builddir}/digdoc
%install
%cmake_install
mkdir -p %{buildroot}/%{_mandir}/man1
install digdoc.1 %{buildroot}/%{_mandir}/man1/digdoc.1
%oreon_autofiles main

%check

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
