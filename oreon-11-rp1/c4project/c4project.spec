%global source0_hash 59e62c94f1c338f68fb2b4edc7f3253974fd91f7144312114b355dcc276dcef0

%global commit 889b315fd9931a961beca0af7df0fe8d96754a5f
%global snapdate 20251002

Name:           c4project
Summary:        Useful CMake scripts
# This project has never been assigned a version. The author really intends it
# for use as a git submodule rather than for system-wide installation.
Version:        0^%{snapdate}.%{sub %{commit} 1 7}
Release:        %autorelease

URL:            https://github.com/biojppm/cmake
# The entire source is MIT, except Toolchain-PS4.cmake and
# Toolchain-XBoxOne.cmake, which are Apache-2.0.
License:        MIT AND Apache-2.0
Source:         %{url}/archive/%{commit}/cmake-%{commit}.tar.gz

BuildArch:      noarch

Requires:       cmake-filesystem
Requires:       git-core

%global common_description %{expand:
%{summary}.}

%description %{common_description}

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n cmake-%{commit}

# For now, we elect not to install the “bm-xp” browser-based benchmark explorer
# tool. It would be inconvenient to package this in a way that was useful in
# practice, and it’s not required by any of the CMake macros that are the real
# point of packaging this.
rm -rvf 'bm-xp'

%build
# Nothing to do

%install
install -d '%{buildroot}%{_datadir}/cmake/c4project'
# We install a copy of the repository, but we don’t want to include dotfiles or
# duplicate the README and LICENSE files.
find . -mindepth 1 -maxdepth 1 ! -name '.*' \( -type d -o \
    -type f ! -name 'README.md' ! -name 'LICENSE.txt' \) \
    -execdir cp -vrp '{}' '%{buildroot}%{_datadir}/cmake/c4project' ';'

%check
# No upstream tests

%files
%license LICENSE.txt
%doc README.md

%{_datadir}/cmake/c4project

%changelog
%autochangelog
