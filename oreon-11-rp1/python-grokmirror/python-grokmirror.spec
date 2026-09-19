%global source0_hash 9de56419f00b77eb408caa57805cd697f07bc05b726a09e7b05237740d47a0a1

Name:           python-grokmirror
Version:        2.0.12
Release:        7%{?dist}
Summary:        Framework to smartly mirror git repositories

# Automatically converted from old format: GPLv3+ - review is highly recommended.
License:        GPL-3.0-or-later
URL:            https://git.kernel.org/pub/scm/utils/grokmirror/grokmirror.git
Source0:        https://www.kernel.org/pub/software/network/grokmirror/grokmirror-%{version}.tar.xz

BuildArch:      noarch
BuildRequires:  python3-devel

%global _description %{expand:
Grokmirror was written to make mirroring large git repository
collections more efficient. Grokmirror uses the manifest file published
by the master mirror in order to figure out which repositories to
clone, and to track which repositories require updating. The process is
extremely lightweight and efficient both for the master and for the
mirrors.}

%description %_description

%package -n python3-grokmirror
Summary:        %summary

%description -n python3-grokmirror %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n grokmirror-%{version}
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files -l grokmirror

mkdir -p -m 0755 %{buildroot}%{_mandir}/man1
install -pm 0644 man/*.1 %{buildroot}/%{_mandir}/man1/

%check
%pyproject_check_import

%files -n python3-grokmirror -f %{pyproject_files}
%license LICENSE.txt
%doc README.rst CHANGELOG.rst UPGRADING.rst grokmirror.conf pi-piper.conf
%{_bindir}/grok-*
%{_mandir}/man1/grok-*.1*

%changelog
%autochangelog
