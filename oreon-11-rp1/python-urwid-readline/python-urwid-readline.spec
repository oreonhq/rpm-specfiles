%global source0_hash f721cbf7825d2dfdb80df2eec1b8a28f4def56db84ce6af94f2392341b4befbb

%global upstream_name urwid_readline
Name:           python-urwid-readline
Version:        0.15.1
Release:        7%{?dist}
Summary:        A textbox edit widget for urwid that supports readline shortcuts

License:        MIT
URL:            https://github.com/rr-/urwid_readline
Source0:        %{url}/archive/%{version}/%{upstream_name}-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  python3-pytest

%global _description %{expand:
A textbox edit widget for urwid that supports readline shortcuts.}

%description %_description

%package -n     python3-urwid-readline
Summary:        %{summary}

%description -n python3-urwid-readline %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{upstream_name}-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{upstream_name}

%check
%pytest

%files -n python3-urwid-readline -f %{pyproject_files}
%doc README.md
%license LICENSE LICENSE.md

%changelog
%autochangelog
