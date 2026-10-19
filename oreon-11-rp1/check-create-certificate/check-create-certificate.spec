%global source0_hash 8b6e1fc13f2cd031cd3e679f6e0f8ce84c1dcee37f83b2ccfec1c51b444aafe3
%global         snapshotdate 20140409
%global         commit d0971baf5d13e06aaa600581efe3adba6631e06a
%global         shortcommit %(c=%{commit}; echo ${c:0:7})
%global         checkout %{snapshotdate}git%{shortcommit}
Name:           check-create-certificate
Version:        0.5
Release:        1%{?dist}
Summary:        A non-interactive script that creates an SSL certificate if it does not exist
License:        GPL-2.0-only
Url:            https://github.com/jdsn/check-create-certificate
Source0:        https://github.com/jdsn/%{name}/archive/%{commit}/%{name}-%{commit}.tar.gz
Requires:       openssl-perl
BuildArch:      noarch
# oreon:deps
BuildRequires:  perl-generators
# /oreon:deps
%description
A script that checks for the existence of an SSL certificate
or creates a new self signed one. It runs non-interactively and
uses either predefined values or automatically guesses the best values.

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{name}-%{commit}

%build

%install
install -Dpm 755 script/%{name} %{buildroot}%{_sbindir}/%{name}
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
