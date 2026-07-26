%global source0_hash c8ba69d592ca20ad35766ce8b5f76c321096cb5f8180d11eb30d8904f4064ecf

%global forgeurl https://github.com/JWCook/requests-ratelimiter/       
%global commit 953c409b0ea205c6b1f2074b5e7cbc97595db5d4

%global pkg_description %{expand:
This package is a simple wrapper around pyrate-limiter v2 that
adds convenient integration with the requests library.
Full project documentation can be found at
requests-ratelimiter.readthedocs.io.
}

Name:           python-requests-ratelimiter
Version:        0.8
Release:        %autorelease
Summary:        Convenient integration with the requests library
License:        MIT
BuildArch:      noarch

%{forgemeta}

Url:     %{forgeurl}
Source0: %{forgesource}

BuildRequires:  %{py3_dist pytest pytest-timeout requests-mock requests-cache}

BuildSystem:    pyproject
BuildOption(install): -l requests_ratelimiter

%description
%{pkg_description}

%package -n python3-requests-ratelimiter
Summary:        Convenient integration with the requests library

%description -n python3-requests-ratelimiter
%{pkg_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{archivename}

%check
%pytest 

%files -n python3-requests-ratelimiter -f %{pyproject_files}
%license LICENSE
%doc README.md

%changelog
%autochangelog
