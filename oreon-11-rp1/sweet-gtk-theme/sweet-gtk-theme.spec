%global source0_hash e1edfcba61328828a4df1a7868f0a412d199efd3085cc0429852c90ef739334c

Name: sweet-gtk-theme
Summary: Light and dark, colorful GTK+ theme
License: GPL-3.0-only
URL: https://www.gnome-look.org/p/1253385/

# Upstream keeps each colour variant of the theme in a separate git branch.
%global git_date_master 20260210
%global git_commit_master a5b3c824ec238f398a5b86e042d8fd74f5496244

%global git_date_ambar 20260210
%global git_commit_ambar b85cd26c87c5d38b3265e4759ceacacf79e03d74

%global git_date_ambar_blue 20260210
%global git_commit_ambar_blue 0c3d02ce438606719db854697aaea87f13a0272a

%global git_date_ambar_blue_dark 20260210
%global git_commit_ambar_blue_dark 3fe9cba71b5dbdfc442e2daa97f80115f530603b

%global git_date_mars 20260210
%global git_commit_mars cff8c309d987cfbedddb62330f9df8d829031e46

%global git_date_nova 20260210
%global git_commit_nova 2c721ad4449ab9e80f4417450270507304ce14c4

%global git_date %( \
	( \
		echo '%{git_date_master}'; \
		echo '%{git_date_ambar}'; \
		echo '%{git_date_ambar_blue}'; \
		echo '%{git_date_ambar_blue_dark}'; \
		echo '%{git_date_mars}'; \
		echo '%{git_date_nova}'; \
	) | sort -rn | head -n1)

Version: 6.0^%{git_date}
Release: 1%{?dist}

%global repo_name  Sweet
%global repo_url   https://github.com/EliverLara/%{repo_name}

Source0: %{repo_url}/archive/%{git_commit_master}/%{repo_name}-Master-%{git_commit_master}.tar.gz
Source1: %{repo_url}/archive/%{git_commit_ambar}/%{repo_name}-Ambar-%{git_commit_ambar}.tar.gz
Source2: %{repo_url}/archive/%{git_commit_ambar_blue}/%{repo_name}-Ambar-Blue-%{git_commit_ambar_blue}.tar.gz
Source3: %{repo_url}/archive/%{git_commit_ambar_blue_dark}/%{repo_name}-Ambar-Blue-Dark-%{git_commit_ambar_blue_dark}.tar.gz
Source4: %{repo_url}/archive/%{git_commit_mars}/%{repo_name}-Mars-%{git_commit_mars}.tar.gz
Source5: %{repo_url}/archive/%{git_commit_nova}/%{repo_name}-Nova-%{git_commit_nova}.tar.gz
Source99: get-sweet-sources.sh

%global variants master ambar ambar-blue ambar-blue-dark mars nova

BuildArch: noarch

BuildRequires: sassc

Recommends: candy-icon-theme

%description
Sweet is a light and dark, colorful GTK+ theme that can be used with
Gnome Shell, Cinnamon, Metacity, xfwm4, and other window managers.

Sweet works great when used together with the Candy icon theme.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%setup -q -c %{repo_name}-%{version} -T -a 0
%setup -q -c %{repo_name}-%{version} -T -D -a 1
%setup -q -c %{repo_name}-%{version} -T -D -a 2
%setup -q -c %{repo_name}-%{version} -T -D -a 3
%setup -q -c %{repo_name}-%{version} -T -D -a 4
%setup -q -c %{repo_name}-%{version} -T -D -a 5

# Rename the directories from "repo-commit" to "branch"
mv "%{repo_name}-%{git_commit_master}" master
mv "%{repo_name}-%{git_commit_ambar}" ambar
mv "%{repo_name}-%{git_commit_ambar_blue}" ambar-blue
mv "%{repo_name}-%{git_commit_ambar_blue_dark}" ambar-blue-dark
mv "%{repo_name}-%{git_commit_mars}" mars
mv "%{repo_name}-%{git_commit_nova}" nova

# Remove executable bits from everything that's not a shell/python script
find ./ -type f -executable \
	'!' '(' -name '*.sh' -o -name '*.fish' -o -name '*.py' ')' \
	-exec chmod --verbose a-x '{}' '+'

%build
# Upstream uses Gulp for building, but it is not available in Fedora.
# The Gulpfile takes care of compiling SASS files, but not much else.
# ...so let's just do that ourselves!
for VARIANT in %{variants}; do
	pushd "${VARIANT}"
	for FILE in \
		gtk-4.0/gtk gtk-4.0/gtk-dark \
		gtk-3.0/gtk gtk-3.0/gtk-dark \
		gnome-shell/gnome-shell \
		cinnamon/cinnamon cinnamon/cinnamon-dark \
	; do
		SCSS_DIR="$(dirname "${FILE}")"
		SCSS_SOURCE="$(basename "${FILE}").scss"
		SCSS_TARGET="${SCSS_SOURCE/scss/css}"

		pushd "${SCSS_DIR}"
		sassc --style=compressed "${SCSS_SOURCE}" "${SCSS_TARGET}"
		popd
	done
	popd
done

%install
for VARIANT in %{variants}; do
	THEME_DIR="%{buildroot}%{_datadir}/themes/Sweet-${VARIANT}"
	install -m 755 -d "${THEME_DIR}"

	pushd "${VARIANT}"
	for FILE in assets cinnamon gnome-shell gtk-2.0 gtk-3.0 gtk-4.0 metacity-1 xfwm4 index.theme; do
		cp -a "${FILE}" "${THEME_DIR}/${FILE}"
	done
	popd

	# Remove all SCSS source files
	# and any executable files that we might have installed by accident
	pushd "${THEME_DIR}"
	find ./ -name '*.scss' -exec rm --verbose '{}' '+'
	find ./ -type f -executable -exec rm --verbose '{}' '+'
	popd
done

# Rename "master" to "classic"
mv "%{buildroot}%{_datadir}/themes/Sweet-master" "%{buildroot}%{_datadir}/themes/Sweet-classic"

%files
%license master/LICENSE
%{_datadir}/themes/Sweet-classic
%{_datadir}/themes/Sweet-ambar
%{_datadir}/themes/Sweet-ambar-blue
%{_datadir}/themes/Sweet-ambar-blue-dark
%{_datadir}/themes/Sweet-mars
%{_datadir}/themes/Sweet-nova

%changelog
%autochangelog
