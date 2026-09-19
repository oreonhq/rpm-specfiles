%global source0_hash 31bb2c9c5a954cb6c29d60218f83ea07be08faac5e2f4431d0463f9adb63fb6e

%global forgeurl https://github.com/asottile/tokenize-rt
Version:        6.2.0
%forgemeta

Name:           python-tokenize-rt
Release:        %autorelease
Summary:        Wrapper for Python's stdlib `tokenize` supporting roundtrips
License:        MIT
URL:            %{forgeurl}
Source:         %{forgesource}

BuildArch:      noarch
BuildRequires:  python3-devel
# Testing requirements
# covdefaults (from tox.ini -> requirements-dev.txt) is not packaged
# for Fedora, using pytest directly
BuildRequires:  python3dist(pytest)

%global _description %{expand:
The stdlib tokenize module does not properly roundtrip. This wrapper
around the stdlib provides two additional tokens ESCAPED_NL and
UNIMPORTANT_WS, and a Token data type. Use src_to_tokens and
tokens_to_src to roundtrip. This library is useful if you are writing
a refactoring tool based on the python tokenization.}

%description %_description

%package -n python3-tokenize-rt
Summary:        %{summary}

%description -n python3-tokenize-rt %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n tokenize-rt-%{version}

%generate_buildrequires
%pyproject_buildrequires -r

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files tokenize_rt

%check
%pytest

%files -n python3-tokenize-rt -f %{pyproject_files}
%doc README.md
%{_bindir}/tokenize-rt

%changelog
%autochangelog
