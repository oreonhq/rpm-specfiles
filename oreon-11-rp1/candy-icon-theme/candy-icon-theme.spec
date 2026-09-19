%global source0_hash 8f26ab2d7fb45b45c10fcc1234b4ba20b50f74808a47d004218c4175eaee7b78

Name:           candy-icon-theme
Summary:        Sweet gradient icon theme
License:        GPL-3.0-only

%global git_repo    candy-icons
%global git_url     https://github.com/EliverLara/%{git_repo}
%global git_commit  b0a85a7414504191342b0c6d073c6f9233cb923a
%global git_date    20260214

%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:7})

Version:        0^%{git_date}.git%{git_commit_short}
Release:        1%{?dist}

URL:            https://www.opendesktop.org/p/1305251/
Source0:        %{git_url}/archive/%{git_commit}/%{git_repo}-%{git_commit}.tar.gz

BuildArch:      noarch

Requires:       adwaita-icon-theme
Requires:       breeze-icon-theme
Requires:       hicolor-icon-theme

%description
Candy Icons is a simplistic, vector, gradient icon theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{git_repo}-%{git_commit}

# Use a prettier name for the theme
sed \
  -e 's|^Name=candy-icons$|Name=Candy Icons|' \
  -i index.theme

%build
# Nothing to do here

%install
CANDY_DIR="%{buildroot}%{_datadir}/icons/Candy"
install -m 755 -d "${CANDY_DIR}"
install -m 644 index.theme "${CANDY_DIR}/"

cp -a -t "${CANDY_DIR}/" \
  apps devices mimetypes places preferences status

touch "${CANDY_DIR}/icon-theme.cache"

%transfiletriggerin -- %{_datadir}/icons/Candy
gtk-update-icon-cache --force %{_datadir}/icons/Candy &>/dev/null || :

%files
%license LICENSE
%dir %{_datadir}/icons/Candy
%{_datadir}/icons/Candy/index.theme
%{_datadir}/icons/Candy/**/*
%ghost %{_datadir}/icons/Candy/icon-theme.cache

%changelog
%autochangelog
