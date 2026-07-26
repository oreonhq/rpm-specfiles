%global source0_hash f5013484eaf7a20eb22d1821aaefe60b50cc329722372b5f8565d46d4aaafcca

Name:           python-wand
Version:        0.6.13
Release:        %autorelease
Summary:        Ctypes-based simple MagickWand API binding for Python

License:        MIT
URL:            https://github.com/emcconville/wand
Source:         %{pypi_source Wand}

BuildArch:      noarch
BuildRequires:  python3-devel
BuildRequires:  ImageMagick-c++-devel
# Documentation
BuildRequires:  texinfo
BuildRequires:  python3dist(docutils)
BuildRequires:  python3dist(sphinx)

%global _description %{expand:
Wand is a ctypes-based simple ImageMagick binding for Python. All
functionalities of MagickWand API are implemented in Wand.}

%description %_description

%package -n     python3-wand
Summary:        %{summary}

%description -n python3-wand %_description

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n Wand-%{version}

%generate_buildrequires
%pyproject_buildrequires -x doc,test

%build
%pyproject_wheel
pushd docs
sphinx-build -b texinfo . texinfo
pushd texinfo
makeinfo --docbook wand.texi	
popd
popd

%install
%pyproject_install
%pyproject_save_files -l wand
mkdir -p %{buildroot}%{_datadir}/help/en/python-wand
install -m644 docs/texinfo/wand.xml %{buildroot}%{_datadir}/help/en/python-wand
cp -p -r docs/texinfo/wand-figures %{buildroot}%{_datadir}/help/en/python-wand/

%check
%pyproject_check_import
%pytest

%files -n python3-wand -f %{pyproject_files}
%doc README.rst
%dir  %{_datadir}/help/en
%lang(en) %{_datadir}/help/en/python-wand

%changelog
%autochangelog
