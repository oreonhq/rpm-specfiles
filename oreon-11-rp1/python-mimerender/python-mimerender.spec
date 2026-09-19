%global source0_hash e7f1377efee18c3f562cee54907a3329223c824332889fb74b745ddfd0a9b1c6

%global srcname mimerender

Name:           python-%{srcname}
Version:        0.6.0
Release:        28%{?dist}
Summary:        RESTful HTTP Content Negotiation for Flask, Bottle, etc.

License:        MIT
URL:            https://pypi.python.org/pypi/%{srcname}
Source0:        https://pypi.python.org/packages/source/m/%{srcname}/%{srcname}-%{version}.tar.gz
# License file is now in the *repo* but not the *tarball*...
Source1:        https://github.com/martinblech/mimerender/blob/v%{version}/LICENSE

BuildArch:      noarch
BuildRequires:  python3-devel

%description
mimerender provides a decorator that wraps a HTTP request handler to select
the correct render function for a given HTTP Accept header. It uses mimeparse
to parse the accept string and select the best available representation.
Supports Flask, Bottle, web.py and webapp2 out of the box, and it’s easy to
add support for other frameworks.

%package -n python3-%{srcname}
Summary:        %{summary}
%{?python_provide:%python_provide python3-%{srcname}}
Requires:       python3-mimeparse
# Note: mimerender has subclasses of MimeRenderBase for web.py, Flask,
# Bottle, and webapp2. When you import 'mimerender', the subclass for
# each framework you have installed will be defined; if the framework
# isn't installed, the subclass for it is skipped (they're all in try/
# except blocks). So if you have python3-flask installed you'll get
# the FlaskMimeRender class, if you have python3-bottle installed you'll
# get BottleMimeRender, and so on. This relationship is not expressed
# through dependencies as it doesn't seem to the packager that such
# dependencies would actually aid in any real-world use of mimeparse;
# if you want to use it in code you've probably already picked a web
# framework, and if it's just being pulled in as a dependency of some
# other package, *that* package will express the appropriate deps on
# the web framework.
#
# Also note that *executing* mimerender.py requires the unittest or
# unittest2 module. All this does is run the test suite (as used in
# check, below). There is no Requires: for this, because it's not
# the expected use of the package, in all normal cases it will be
# used by importing the module.

%description -n python3-%{srcname}
mimerender provides a decorator that wraps a HTTP request handler to select
the correct render function for a given HTTP Accept header. It uses mimeparse
to parse the accept string and select the best available representation.
Supports Flask, Bottle, web.py and webapp2 out of the box, and it’s easy to
add support for other frameworks. This is the Python 3 build of mimerender.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version}
cp %{SOURCE1} ./LICENSE

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{srcname}

%check
%{__python3} src/mimerender.py

%files -n python3-%{srcname} -f %{pyproject_files}
%license LICENSE

%changelog
%autochangelog
