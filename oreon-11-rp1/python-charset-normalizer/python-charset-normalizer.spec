%global source0_hash 5bfb2fc7b4cb63254fc58302223cd3d654766cac56ae6aac29ca37911ba5b3ab

Name:           python-charset-normalizer
Version:        3.5.1
Release:        %autorelease
Summary:        The Real First Universal Charset Detector
# SPDX
License:        MIT
URL:            https://github.com/ousret/charset_normalizer
Source0:        https://github.com/ousret/charset_normalizer/archive/refs/tags/3.4.6.tar.gz#/python-charset-normalizer-3.4.6.tar.gz
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3dist(pytest)


%description
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking
a new approach. All IANA character set names for which the Python core
library provides codecs are supported.

%package -n     python3-charset-normalizer
Summary:        %{summary}

%description -n python3-charset-normalizer
A library that helps you read text from an unknown charset encoding.
Motivated by chardet, trying to resolve the issue by taking
a new approach. All IANA character set names for which the Python core
library provides codecs are supported.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }
%autosetup -n charset_normalizer-%{version}
# Drop mypy from build dependencies
sed -i 's/"mypy.*"//' pyproject.toml

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files charset_normalizer

%check
%pytest

%files -n python3-charset-normalizer -f %{pyproject_files}
%license LICENSE
%doc README.md
%{_bindir}/normalizer

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 3.4.6-1
- Prepare for Oreon 11 (RP1)
