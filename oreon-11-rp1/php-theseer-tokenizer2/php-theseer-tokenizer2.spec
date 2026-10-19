%global source0_hash a8a470b00d68fc86300fc73b3aa19392b4683a608bcfc94e941c7ed5c5328dd7
%bcond_without       tests
%global gh_commit    7989e43bf381af0eac72e4f0ca5bcbfa81658be4
%global gh_short     %(c=%{gh_commit}; echo ${c:0:7})
%global gh_vendor    theseer
%global gh_project   tokenizer
%global ns_vendor    TheSeer
%global ns_project   Tokenizer
%global major        2
Name:           php-%{gh_vendor}-%{gh_project}%{major}
Version:        2.0.1
Release:        1%{?dist}
Summary:        Library for converting tokenized PHP source code into XML
License:        BSD-3-Clause
URL:            https://github.com/%{gh_vendor}/%{gh_project}
Source0:        %{name}-%{version}-%{gh_short}.tgz
Source1:        makesrc.sh
BuildArch:      noarch
%if %{with tests}
%endif
Requires:       php(language) >= 8.1
Requires:       php-xmlwriter
Requires:       php-dom
Requires:       php-tokenizer
Requires:       php-composer(fedora/autoloader)
Provides:       php-composer(%{gh_vendor}/%{gh_project}) = %{version}
# oreon:deps
BuildRequires:  php(language)
BuildRequires:  php-dom
BuildRequires:  php-fedora-autoloader-devel
BuildRequires:  php-tokenizer
BuildRequires:  php-xmlwriter
BuildRequires:  phpunit9
# /oreon:deps
%description
A small library for converting tokenized PHP source code into XML
and potentially other formats.

Autoloader: %{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{gh_project}-%{gh_commit}

%build

: Generate a simple classmap autoloader
%{_bindir}/phpab --template fedora --output src/autoload.php src
%install
mkdir -p   %{buildroot}%{_datadir}/php/%{ns_vendor}
cp -pr src %{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}
%oreon_autofiles main
%if %{with tests}
%check

ret=0
for cmdarg in php php81 php82 php83 php84 php85; do
  if which $cmdarg; then
      $cmdarg -d auto_prepend_file=%{buildroot}%{_datadir}/php/%{ns_vendor}/%{ns_project}%{major}/autoload.php \
        %{_bindir}/phpunit9 \
          --no-coverage --verbose || ret=1
  fi
done
exit $ret
%endif
%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
