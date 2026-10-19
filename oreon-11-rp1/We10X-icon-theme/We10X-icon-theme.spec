%global source0_hash 77a103035d9628423d3ca080e09eb73b262bdc1fe51bfe34ae8b86990109f91c
Name:    We10X-icon-theme
Summary:        Colorful icon theme inspired by Microsoft Windows 10 aesthetic
License: GPL-3.0-only
%global git_date    20251114
%global git_commit  0f52ff2dce554146f8f76ab2c7a5968fd773400d
%global git_commit_short  %(c="%{git_commit}"; echo ${c:0:7})
Version: 0^%{git_date}.git%{git_commit_short}
Release:        3%{?dist}
URL: https://github.com/yeyushengfan258/%{name}
Source0:        https://github.com/yeyushengfan258/%{name}/archive/%{git_commit}/%{name}-%{git_commit}.tar.gz
Patch0: 0000-install-fix.patch
BuildArch: noarch
Requires: hicolor-icon-theme
# oreon:deps

# /oreon:deps
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

%install
install -m 755 -d '%{buildroot}%{_datadir}/icons'
./install.sh --dest '%{buildroot}%{_datadir}/icons'
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
	find ./ -follow -type l -printf 'deleted broken symlink "%p" -> "%l"\n' -delete
	touch icon-theme.cache
	rm AUTHORS COPYING
	popd
done
%transfiletriggerin -- %{_datadir}/icons/We10X
gtk-update-icon-cache --force %{_datadir}/icons/We10X &>/dev/null || :
%transfiletriggerin -- %{_datadir}/icons/We10X-dark
gtk-update-icon-cache --force %{_datadir}/icons/We10X-dark &>/dev/null || :
%oreon_autofiles main

%files -f %{oreon_filedir}/main.list

%changelog

%autochangelog
