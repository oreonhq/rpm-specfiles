%global source0_hash e9dcaddf1820392eeabba81774b694265546f1e20e297564226b8c1ae0f8cd86

Name:           python-moddb
Version:        0.12.0
Release:        6%{?dist}
Summary:        A Python scraper/parser for ModDB
License:        MIT
URL:            https://github.com/ClementJ18/moddb
Source0:        %{url}/archive/v%{version}/moddb-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
%global _description %{expand:
                       The goal of the library is to be able to navigate ModDB purely
                       programmatically through scraping and parsing of the various models
                       present on the website. This is based off a command of a bot which
                       can parse either a game or a mod, this command gave birth to the
                       original library which was extremely limited in its abilities and
                       only able to parse a few pages with inconsistencies. This library
                       is a much more mature and professional attempt at the whole idea,
                       adding on a much deeper understanding of OOP.}

%description %{_description}

%package -n python3-moddb
Summary:        %{summary}

%description -n python3-moddb %{_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n moddb-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files moddb

%check
# Upstream tests generally require network access and authentication
%pyproject_check_import

%files -n python3-moddb -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
