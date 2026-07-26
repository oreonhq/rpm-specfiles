%global source0_hash cbc1fef89f8d062739774bd51eda3da3274006b3661d199c2655f6b3f6d605a0

%global         pypi_name langdetect

Name:           python-%{pypi_name}
Version:        1.0.9
Release:        16%{?dist}
Summary:        Language detection library ported from Google's language-detection

# Both python-langdetect and language-detection are under ASL 2.0
License:        Apache-2.0
URL:            https://pypi.org/project/langdetect/
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires:  python3dist(pytest)
BuildRequires:  python3dist(six)

%generate_buildrequires
%pyproject_buildrequires

%global _description %{expand:
Port of Nakatani Shuyo's language-detection library (version from 03/03/2014) to
Python.

langdetect supports 55 languages out of the box (ISO 639-1 codes):
af, ar, bg, bn, ca, cs, cy, da, de, el, en, es, et, fa, fi, fr, gu, he, hi, hr,
hu, id, it, ja, kn, ko, lt, lv, mk, ml, mr, ne, nl, no, pa, pl, pt, ro, ru, sk,
sl, so, sq, sv, sw, ta, te, th, tl, tr, uk, ur, vi, zh-cn, zh-tw}

%description %{_description}

%package -n python3-%{pypi_name}
Summary:        %{summary}

%description -n python3-%{pypi_name} %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{pypi_name}-%{version}

#rm -rf %{pypi_name}.egginfo

chmod 644 LICENSE NOTICE langdetect/profiles/*

%build
%pyproject_wheel

%install
%pyproject_install

%check
%pytest

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE NOTICE
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}.dist-info/

%changelog
%autochangelog
