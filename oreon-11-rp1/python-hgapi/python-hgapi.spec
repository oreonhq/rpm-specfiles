%global source0_hash 0b1f20a6a8cefe9e9f72b14a0823b7abdbc88d19cdf815211849067d9ac27ebc

Name:           python-hgapi
Version:        1.7.4
Release:        33%{?dist}
Summary:        Python API to Mercurial using the command-line interface

License:        MIT
URL:            https://bitbucket.org/haard/hgapi
Source0:        https://files.pythonhosted.org/packages/36/db/6ad72214343e361c3fae732230e64bb7a5e4580002027782a4406748aee6/hgapi-1.7.4.tar.gz
Source1:        LICENSE

BuildArch:      noarch

%global _description\
hgapi is a pure-Python API to Mercurial, that uses the command-line interface\
instead of the internal Mercurial API. The rationale for this is twofold: the\
internal API is unstable, and it is GPL.\
\
hgapi works for all versions of Mercurial, and will instantly reflect any\
changes to the repository (including hgrc).

%description %_description

%package -n     python3-hgapi
Summary:        Python 3 API to Mercurial using the command-line interface
BuildRequires:  python3-devel
BuildRequires:  mercurial
Requires:       mercurial

%description -n python3-hgapi
hgapi is a pure-Python API to Mercurial, that uses the command-line interface
instead of the internal Mercurial API. The rationale for this is twofold: the
internal API is unstable, and it is GPL.

hgapi works for all versions of Mercurial, and will instantly reflect any
changes to the repository (including hgrc).

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -n hgapi-%{version}
cp %{SOURCE1} .
# Remove egg
# Apply patch
sed -i 's/\r$//' hgapi/testhgapi.py
# Correct end of line encoding for README.rst
sed -i 's/\r$//' README.rst

rm -rf %{py3dir}
cp -a . %{py3dir}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

%check

%files -n python3-hgapi
%doc README.rst
%license LICENSE
%{python3_sitelib}/hgapi-%{version}.dist-info/
%{python3_sitelib}/hgapi/

%changelog
%autochangelog
