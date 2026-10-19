%global source0_hash 1238259d9d979f35edd4ff6667467d48f4246aa98a50e17b3c4c97b2c105fbb5
Name:           python-pymapvbvd
Version:        0.6.1
Release:        1%{?dist}
Summary:        Python twix file reader
License:        MIT AND Unlicense
URL:            https://github.com/wtclarke/pymapvbvd
Source0:        https://files.pythonhosted.org/packages/source/p/pymapvbvd/pymapvbvd-%{version}.tar.gz
Source1:        pymapvbvd-test-data.tar.zst
Source2:        get_test_data.sh
BuildArch:      noarch
ExcludeArch:    s390x
%global common_description %{expand:
Python port of the Matlab mapVBVD tool for reading Siemens raw data 'twix'
(.dat) files.}
# oreon:deps

# /oreon:deps
%description %{common_description}

%package -n python3-pymapvbvd
Summary:        Python twix file reader
%py_provides python3-mapvbvd
%description -n python3-pymapvbvd %{common_description}

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n pymapvbvd-%{version} -p1
%setup -q -T -D -a 1 -c -n pymapvbvd-%{version}
# We can use the system versioneer to generate _version.py, and can remove the
# bundled, amaglamated versioneer.py to indicate we aren’t using it.
rm -v versioneer.py

%build -p

export SETUPTOOLS_SCM_PRETEND_VERSION='%{version}'
%install
%pyproject_install
%oreon_autofiles python3-pymapvbvd usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

%pytest -v
%files -f %{oreon_filedir}/main.list
%files -n python3-pymapvbvd -f %{oreon_filedir}/python3-pymapvbvd.list

%changelog

%autochangelog
