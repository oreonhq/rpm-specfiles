%global source0_hash 97cfbb82cbbb715019a790a59af4dc3ba6bd07c037ea892ba4dc092259bb6301

Name:           msm-cros-efs-loader
Version:        1.0.2
Release:        %autorelease
Summary:        EFS loader for Qualcomm-based Chrome OS devices

License:        GPL-3.0-or-later
URL:            https://gitlab.postmarketos.org/postmarketOS/msm-cros-efs-loader

Source:         %{url}/-/archive/v%{version}/%{name}-v%{version}.tar.gz

BuildArch:      noarch

%description
EFS loader for Qualcomm-based Chrome OS devices

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-v%{version}

%install
install -D -p -m 0755 msm-cros-efs-loader.sh %{buildroot}%{_bindir}/%{name}

%files
%license LICENSE
%{_bindir}/%{name}

%changelog
%autochangelog
