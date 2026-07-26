%global source0_hash 2634b4b8b3d69a397f5462ec1d72a77d5b395f363ed8e1aabfbf7e5e4172f93f

%global forgeurl https://github.com/fboender/multi-git-status
Version:         2.3

%forgemeta

Name:            multi-git-status
Release:         4%{?dist}
Summary:         Show uncommitted, untracked and unpushed changes for multiple Git repos
URL:             %{forgeurl}
Source:          https://github.com/fboender/multi-git-status/archive/%{name}-%{version}.tar.gz
License:         MIT
BuildArch:       noarch

Requires:        coreutils
Requires:        findutils
Requires:        gawk
Requires:        git
Requires:        sed

%description
Show uncommitted, untracked and unpushed changes for multiple Git repos.

multi-git-status shows:
* Uncommitted changes if there are unstaged or uncommitted changes on the
  checked out branch.
* Untracked files if there are untracked files which are not ignored.
* Needs push (BRANCH) if the branch is tracking a (remote) branch which is
  behind.
* Needs upstream (BRANCH) if a branch does not have a local or remote
  upstream branch configured. Changes in the branch may otherwise
  never be pushed or merged.
* Needs pull (BRANCH) if the branch is tracking a (remote) branch which is
  ahead. This requires that the local git repo already knows about the remote
  changes (i.e. you've done a fetch), or that you specify the -f option.
  Multi-git-status does NOT contact the remote by default.
* X stashes if there are stashes.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%forgesetup

%build

%install
install -p -D -m755 mgitstatus %{buildroot}%{_bindir}/mgitstatus
install -p -D -m755 mgitstatus.1 %{buildroot}%{_mandir}/man1/mgitstatus.1

%files
%{_bindir}/mgitstatus
%license LICENSE.txt
%doc README.md
%doc screenshot.png
%doc %{_mandir}/man1/mgitstatus.1*

%changelog
%autochangelog
