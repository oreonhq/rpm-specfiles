%global source0_hash 77a103035d9628423d3ca080e09eb73b262bdc1fe51bfe34ae8b86990109f91c

Name:    We10X-icon-theme
Summary: Colorful icon theme inspired by Microsoft Windows 10 aesthetic
License: GPL-3.0-only

%global git_date    20251114
%global git_commit  0f52ff2dce554146f8f76ab2c7a5968fd773400d
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:7})

Version: 0^%{git_date}.git%{git_commit_short}
Release: 3%{?dist}

URL: https://github.com/yeyushengfan258/%{name}
Source0: %{url}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz

# Fix install script producing absolute symlinks
Patch0: 0000-install-fix.patch

BuildArch: noarch

Requires: hicolor-icon-theme

%description
We10X is a colorful icon theme inspired
by the aesthetic of Microsoft Windows 10.

Comes in a regular and dark variant.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{name}-%{git_commit}

# Remove spurious executable bits found on some files
chmod 644 ./AUTHORS ./COPYING
find links/ src/ -executable -type f -exec chmod -v -- a-x '{}' '+'

# Do not call gtk-update-icon-cache during install
sed  \
	-e '/gtk-update-icon-cache/d'  \
	-i install.sh

%build
# Nothing to do here

%install
install -m 755 -d '%{buildroot}%{_datadir}/icons'
./install.sh --dest '%{buildroot}%{_datadir}/icons'

# Some icon categories used to have separate versions for classic
# and dark variant of the theme. Later, upstream decided to use the same
# icons for both, replacing the dark version's directory with a symlink.
# This makes RPM throw an error when trying to update the package,
# as it refuses to replace a directory with a symlink.
#
# For each affected category, if the -dark directory is a symlink,
# replace it with a directory filled with file symlinks.
for CATEGORY in status/16 status/22 status/24; do
	CATEGORY_DIR="%{buildroot}%{_datadir}/icons/We10X-dark/${CATEGORY}"
	if [[ -L "${CATEGORY_DIR}" ]]; then
		rm "${CATEGORY_DIR}"
		install -m 755 -d "${CATEGORY_DIR}"

		for FILE in "%{buildroot}%{_datadir}/icons/We10X/${CATEGORY}/"* ; do
			ln -sr "${FILE}" "${CATEGORY_DIR}/"
		done
	fi
done

for VARIANT in '' '-dark'; do
	pushd "%{buildroot}%{_datadir}/icons/We10X${VARIANT}"

	# Remove broken symlinks
	find ./ -follow -type l -printf 'deleted broken symlink "%p" -> "%l"\n' -delete

	# Create empty file for the cache
	touch icon-theme.cache

	# Remove these files (we will include them via %%doc/%%license macros)
	rm AUTHORS COPYING
	popd
done

%transfiletriggerin -- %{_datadir}/icons/We10X
gtk-update-icon-cache --force %{_datadir}/icons/We10X &>/dev/null || :

%transfiletriggerin -- %{_datadir}/icons/We10X-dark
gtk-update-icon-cache --force %{_datadir}/icons/We10X-dark &>/dev/null || :

%files
%doc AUTHORS
%license COPYING

# -- normal variant

%dir %{_datadir}/icons/We10X
%ghost %{_datadir}/icons/We10X/icon-theme.cache
%{_datadir}/icons/We10X/index.theme

%{_datadir}/icons/We10X/actions
%{_datadir}/icons/We10X/actions@2x
%{_datadir}/icons/We10X/animations
%{_datadir}/icons/We10X/animations@2x
%{_datadir}/icons/We10X/apps
%{_datadir}/icons/We10X/apps@2x
%{_datadir}/icons/We10X/categories
%{_datadir}/icons/We10X/categories@2x
%{_datadir}/icons/We10X/devices
%{_datadir}/icons/We10X/devices@2x
%{_datadir}/icons/We10X/emblems
%{_datadir}/icons/We10X/emblems@2x
%{_datadir}/icons/We10X/emotes
%{_datadir}/icons/We10X/emotes@2x
%{_datadir}/icons/We10X/mimes
%{_datadir}/icons/We10X/mimes@2x
%{_datadir}/icons/We10X/places
%{_datadir}/icons/We10X/places@2x
%{_datadir}/icons/We10X/preferences
%{_datadir}/icons/We10X/preferences@2x
%{_datadir}/icons/We10X/status
%{_datadir}/icons/We10X/status@2x

# -- dark variant

%dir %{_datadir}/icons/We10X-dark
%ghost %{_datadir}/icons/We10X-dark/icon-theme.cache
%{_datadir}/icons/We10X-dark/index.theme

%{_datadir}/icons/We10X-dark/actions
%{_datadir}/icons/We10X-dark/actions@2x
%{_datadir}/icons/We10X-dark/animations
%{_datadir}/icons/We10X-dark/animations@2x
%{_datadir}/icons/We10X-dark/apps
%{_datadir}/icons/We10X-dark/apps@2x
%{_datadir}/icons/We10X-dark/categories
%{_datadir}/icons/We10X-dark/categories@2x
%{_datadir}/icons/We10X-dark/devices
%{_datadir}/icons/We10X-dark/devices@2x
%{_datadir}/icons/We10X-dark/emblems
%{_datadir}/icons/We10X-dark/emblems@2x
%{_datadir}/icons/We10X-dark/emotes
%{_datadir}/icons/We10X-dark/emotes@2x
%{_datadir}/icons/We10X-dark/mimes
%{_datadir}/icons/We10X-dark/mimes@2x
%{_datadir}/icons/We10X-dark/places
%{_datadir}/icons/We10X-dark/places@2x
%{_datadir}/icons/We10X-dark/preferences
%{_datadir}/icons/We10X-dark/preferences@2x
%{_datadir}/icons/We10X-dark/status
%{_datadir}/icons/We10X-dark/status@2x

%changelog
%autochangelog
