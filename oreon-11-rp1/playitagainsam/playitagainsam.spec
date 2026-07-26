%global source0_hash caabc9d648941f5acf8f821057d352c2f8e3a8d86db96c20efbf08626ef65cc9

Name:           playitagainsam
Version:        0.6.0
Release:        %autorelease
Summary:        Record and replay interactive terminal sessions

License:        MIT
URL:            https://github.com/rfk/playitagainsam
Source0:        %{pypi_source playitagainsam}
BuildArch:      noarch

BuildRequires:  python3-devel

# shortcut and executable name
Provides:       pias = %{version}-%{release}

%description
Playitagainsam is a tool and a corresponding file format for recording and
replaying interactive terminal sessions. It takes inspiration from the Unix
commands "script" and "ttyrec" and the Python tool "playerpiano".

Useful features include:

 * ability to replay with fake typing for enhanced "interactivity"
 * ability to replay synchronized output in multiple terminals

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{name}-%{version}

# Shebang removal
sed -i '1d' %{name}/__main__.py

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files playitagainsam

%check
%pyproject_check_import

%files -f %{pyproject_files}
%doc README.rst ChangeLog.txt
%{_bindir}/pias

%changelog
%autochangelog
