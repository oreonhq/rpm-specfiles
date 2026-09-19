%global source0_hash b23309773041a68225a11eace086d441db0694f63f38043da3b2ed6a0f5f2d71

Name:		php-liuggio-statsd-php-client
Version:	1.0.18
Release:	23%{?dist}
Summary:	Object Oriented Client for etsy/statsd written in php

License:	MIT
URL:		https://github.com/liuggio/statsd-php-client
Source0:	https://github.com/liuggio/statsd-php-client/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Source1:	%{name}-autoload.php

BuildArch:	noarch

BuildRequires:	phpunit10
# https://pagure.io/releng/issue/12229
#BuildRequires:	php-composer(symfony/class-loader)
#BuildRequires:	php-composer(monolog/monolog) >= 1.2.0

Requires:	php(language) >= 5.3.2
Requires:	php-pcre
Requires:	php-sockets
Requires:	php-spl

Provides:	php-composer(liuggio/statsd-php-client) = %{version}

%description
statsd-php-client is an Open Source, and Object Oriented Client for etsy/statsd
written in php.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn statsd-php-client-%{version}

%build

%install
mkdir -pm 0755 %{buildroot}%{_datadir}/php/Liuggio/StatsdClient
cp -rp src/Liuggio/StatsdClient/* %{buildroot}%{_datadir}/php/Liuggio/StatsdClient
cp -p %{SOURCE1} %{buildroot}%{_datadir}/php/Liuggio/StatsdClient/autoload.php

#check
#phpunit -v \
#    --bootstrap=%%{buildroot}%%{_datadir}/php/Liuggio/StatsdClient/autoload.php

%files
%license LICENSE
%doc CHANGELOG.md composer.json README.md
%{_datadir}/php/Liuggio

%changelog
%autochangelog
