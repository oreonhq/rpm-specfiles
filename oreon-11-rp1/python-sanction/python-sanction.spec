%global source0_hash 8b03991f382575137a22cd09a3a13d8e25a11ccaa173b987e4f19a4885eabb21

%global modname sanction

Name:               python-sanction
Version:            0.4.1
Release:            16%{?dist}
Summary:            A simple, lightweight OAuth2 client
License:            MIT
URL:                http://pypi.python.org/pypi/sanction
Source0:            https://github.com/demianbrecht/%{modname}/archive/refs/tags/%{version}.tar.gz

BuildArch:          noarch

BuildRequires:      python3-devel
BuildRequires:      python3-setuptools

%global _description\
python-sanction is a lightweight, dead simple client implementation of\
the OAuth2 protocol.\
\
- Variations on OAuth2 client implementation range from a few hundred LOC\
  to thousands. In a Pythonic world, there's absolutely no need for this when\
  simply dealing with the client side of the spec. Currently, sanction sits\
  at a whopping 65 LOC, one class. This makes the library tremendously easy\
  to grok.\
\
- Most providers have varying levels of diversion from the official spec.\
  The goal with this library is to either handle these diversions natively,\
  or expose a method to allow client code to deal with it efficiently and\
  effectively.\
\
- Three of the four OAuth2 flows should be supported by this library.\
  Currently, only authorization code and client credential flows have been\
  tested due to lack of other (known) implementations.\
\
sanction has been tested with the following OAuth2 providers:\
\
* Facebook (include the test API)\
* Google\
* Foursquare\
* bitly\
* GitHub\
* StackExchange\
* Instagram\
* DeviantArt

%description %_description

%package -n python3-sanction
Summary:            A simple, lightweight OAuth2 client

%description -n python3-sanction
python-sanction is a lightweight, dead simple client implementation of
the OAuth2 protocol.

- Variations on OAuth2 client implementation range from a few hundred LOC
  to thousands. In a Pythonic world, there's absolutely no need for this when
  simply dealing with the client side of the spec. Currently, sanction sits
  at a whopping 65 LOC, one class. This makes the library tremendously easy
  to grok.

- Most providers have varying levels of diversion from the official spec.
  The goal with this library is to either handle these diversions natively,
  or expose a method to allow client code to deal with it efficiently and
  effectively.

- Three of the four OAuth2 flows should be supported by this library.
  Currently, only authorization code and client credential flows have been
  tested due to lack of other (known) implementations.

sanction has been tested with the following OAuth2 providers:

* Facebook (include the test API)
* Google
* Foursquare
* bitly
* GitHub
* StackExchange
* Instagram
* DeviantArt

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

# Use the standard library instead of a backport
  sed -i -e 's/^import mock/from unittest import mock/' \
         -e 's/^from mock import /from unittest.mock import /' \
      %{modname}/test.py tests.py

%build
%py3_build

%install
%py3_install

%check
%{python3} -m unittest discover -v

%files -n python3-sanction
%doc README LICENSE
%{python3_sitelib}/%{modname}/
%{python3_sitelib}/%{modname}-%{version}*

%changelog
%autochangelog
