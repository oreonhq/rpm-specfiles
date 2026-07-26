%global source0_hash 4cf17c82fb9646d1bc9ca92ac280813a3b605d8c421225fd9913154103ee1fbd

# DOCUMENTATION NOTE: We used to build the documentation, but then upstream
# started depending on sphinx-book-theme, which we do not have in Fedora.
# Packaging it would require adding about 3 dozen new packages to Fedora, which
# is more work than I want to go to for this package, which I only need to
# generate documentation for another package.

Name:           python-sphinx-copybutton
Version:        0.5.2
Release:        %autorelease
Summary:        Add a copy button to code cells in Sphinx docs

License:        MIT
URL:            https://sphinx-copybutton.readthedocs.io/en/latest/
Source0:        %{pypi_source sphinx-copybutton}

BuildArch:      noarch
BuildRequires:  python3-devel

# This can be removed when F38 reaches EOL
Obsoletes:      %{name}-doc < 0.3.2
Provides:       %{name}-doc = %{version}-%{release}

# the [code_style] extra is only used for checking code style of this package
# the [rtd] is only used to generate docs on readthedocs.org
# as of 0.5.0, there are no more extras

%global _description %{expand:
Sphinx-copybutton does one thing: add a little "copy" button to the
right of your code blocks.  If the code block overlaps to the right of
the text area, you can just click the button to get the whole thing.}

%description %_description

%package     -n python3-sphinx-copybutton
Summary:        %{summary}

%description -n python3-sphinx-copybutton %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n sphinx-copybutton-%{version}

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files sphinx_copybutton

%check
%pyproject_check_import

%files -n python3-sphinx-copybutton -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
