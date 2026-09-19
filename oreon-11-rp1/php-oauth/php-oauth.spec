%global source0_hash 37540698456f87744e99cc0ad1f646f943ef81d72da439a2bd9adbad7e472ea5

%global realname    oauth
%global svnrevision svn1271

Name:           php-oauth
Version:        1.0
Release:        0.36.%{svnrevision}%{?dist}
Summary:        PHP Authentication library for desktop to web applications

License:        MIT
URL:            http://code.google.com/p/oauth/

# Package tarball not present. To compress:
# svn export -r 1271 http://oauth.googlecode.com/svn/code/php/ oauth-svn1271
# tar -czf php-oauth-svn1271.tar.gz oauth-svn1271
Source0:        %{name}-%{svnrevision}.tar.gz

BuildArch:      noarch
Requires:       php-date
Requires:       php-hash
Requires:       php-openssl
Requires:       php-pcre
Requires:       php-spl

%description
An open protocol to allow API authentication in a simple and standard
method from desktop and web applications.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -qn %{realname}-%{svnrevision}
mv OAuth_TestServer.php example

%build
# Empty build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{_datadir}/php/%{realname}
install -p -m 644 OAuth.php %{buildroot}%{_datadir}/php/%{realname}/

%files
%doc doc example *txt
%{_datadir}/php/%{realname}

%changelog
%autochangelog
