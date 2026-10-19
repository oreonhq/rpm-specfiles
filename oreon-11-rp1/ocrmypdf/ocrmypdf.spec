%global source0_hash aca73a23a80cf2f46a4c15040b0035203dbf74054b7a0c3a7ee93b05abc555a6
%global srcname ocrmypdf
Name:           %{srcname}
Version:        17.12.1
Release:        1%{?dist}
Summary:        Add an OCR text layer to scanned PDF files
License:        MPL-2.0 AND Zlib
URL:            https://github.com/ocrmypdf/OCRmyPDF
Source0:        https://files.pythonhosted.org/packages/source/o/%{name}/%{name}-%{version}.tar.gz
Patch:          0001-Remove-unnecessary-dependencies.patch
Patch:          ocrmypdf-16.12.0-no-typer-slim.patch
BuildArch:      noarch
ExcludeArch: %{ix86}
Requires:       ghostscript >= 9.15
Recommends:     pngquant >= 2.0.0
Requires:       tesseract >= 4.1.1
Recommends:     unpaper >= 6.1
Obsoletes:      ocrmypdf+webservice < 16.7.0-3
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-ocrmypdf = %{version}-%{release}
# /oreon:deps
%package -n       python3-ocrmypdf+heic
Summary:        Metapackage for python3-ocrmypdf heic extras
Requires:       python3-ocrmypdf = %{version}-%{release}
Requires:       python3dist(pillow-heif) >= 1.7.0
Provides:       python3dist(ocrmypdf[heic]) = %{version}-%{release}

%description -n python3-ocrmypdf+heic
Metapackage for python3-ocrmypdf heic extras.

%package -n       python3-ocrmypdf+watcher
Summary:        Metapackage for python3-ocrmypdf watcher extras
Requires:       python3-ocrmypdf = %{version}-%{release}
Requires:       python3dist(watchfiles) >= 1.0
Requires:       python3dist(cyclopts) >= 3
Provides:       python3dist(ocrmypdf[watcher]) = %{version}-%{release}

%description -n python3-ocrmypdf+watcher
Metapackage for python3-ocrmypdf watcher extras.

%package -n       python3-ocrmypdf+webservice
Summary:        Metapackage for python3-ocrmypdf webservice extras
Requires:       python3-ocrmypdf = %{version}-%{release}
Requires:       python3dist(streamlit) >= 1.41.0
Provides:       python3dist(ocrmypdf[webservice]) = %{version}-%{release}

%description -n python3-ocrmypdf+webservice
Metapackage for python3-ocrmypdf webservice extras.

%description
OCRmyPDF adds an OCR text layer to scanned PDF files, allowing them to be
searched or copy-pasted.

%package -n %{srcname}-doc
Summary:        ocrmypdf documentation
License:        CC-BY-SA-4.0
%description -n %{srcname}-doc
Documentation for ocrmypdf

%{_bindir}/%{srcname}-watcher

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{srcname}-%{version} -p1

# Cleanup shebang and executable bits.
for f in src/%{srcname}/*.py src/%{srcname}/*/*.py; do
    sed -e '1{\@^#!/usr/bin/env python@d}' $f > $f.new &&
    touch -r $f $f.new &&
    mv $f.new $f
    chmod -x $f
done

%build

%pyproject_wheel
PYTHONPATH="$PWD/build/lib" OCRMYPDF_VERSION="%{version}" sphinx-build-3 docs html
rm -rf html/.{doctrees,buildinfo}
%install
%pyproject_install
install -Dpm 0644 misc/completion/ocrmypdf.bash %{buildroot}%{_datadir}/bash-completion/completions/ocrmypdf
install -Dpm 0644 misc/completion/ocrmypdf.fish %{buildroot}%{_datadir}/fish/vendor_completions.d/ocrmypdf.fish
install -Dpm 0755 misc/watcher.py %{buildroot}%{_bindir}/%{srcname}-watcher
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

k="${k-}${k+ and }not test_tesseract_config_invalid"
%{pytest} -ra -n auto --runslow -k "${k-}"
%files
%files -n ocrmypdf-doc -f %{oreon_filedir}/ocrmypdf-doc.list

%changelog

%autochangelog
