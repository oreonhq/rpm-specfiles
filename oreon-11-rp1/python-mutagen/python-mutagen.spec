%global source0_hash 719fadef0a978c31b4cf3c956261b3c58b6948b32023078a2117b1de09f0fc99

%global modname mutagen
# Share doc between python2- and python3-
%global _docdir_fmt %{name}

Name:           python-%{modname}
Version:        1.47.0
Release:        12%{?dist}
Summary:        Mutagen is a Python module to handle audio meta-data

# licensecheck -r . | grep -vEe "UNKNOWN" -e "GNU General Public License v2.0" | sort
#
# ./mutagen/_senf/_argv.py: MIT License
# ./mutagen/_senf/_compat.py: MIT License
# ./mutagen/_senf/_environ.py: MIT License
# ./mutagen/_senf/_fsnative.py: MIT License
# ./mutagen/_senf/__init__.py: MIT License
# ./mutagen/_senf/_print.py: MIT License
# ./mutagen/_senf/_stdlib.py: MIT License
# ./mutagen/_senf/_temp.py: MIT License
# ./mutagen/_senf/_winansi.py: MIT License
# ./mutagen/_senf/_winapi.py: MIT License
License:        GPL-2.0-or-later AND MIT
URL:            https://github.com/quodlibet/mutagen
Source0:        %{url}/releases/download/release-%{version}/%{modname}-%{version}.tar.gz

BuildArch:      noarch

%global _description \
Mutagen is a Python module to handle audio meta-data. It supports\
reading ID3 (all versions), APEv2, FLAC, and Ogg Vorbis/FLAC/Theora.\
It can write ID3v1.1, ID3v2.4, APEv2, FLAC, and Ogg Vorbis/FLAC/Theora\
comments. It can also read MPEG audio and Xing headers, FLAC stream\
info blocks, and Ogg Vorbis/FLAC/Theora stream headers. Finally, it\
includes a module to handle generic Ogg bit-streams.

%description %{_description}

%package -n python3-%{modname}
Summary:        %{summary}
BuildRequires:  python3-devel
BuildRequires:  python3-hypothesis
BuildRequires:  python3-pytest
BuildRequires:  python3-sphinx_rtd_theme
Obsoletes:      python2-mutagen < 1.42.0-10

%description -n python3-%{modname} %{_description}

Python 3 version.

%package doc
Summary:        Documentation for python-mutagen
BuildRequires:  /usr/bin/sphinx-build

%description doc
Contains the html documentation for python mutagen.

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n %{modname}-%{version} -p1

%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

sphinx-build -b html -n docs docs/_build

%install
%pyproject_install
%pyproject_save_files -l %{modname}

install -D -p -m 0644 man/*.1 %{buildroot}%{_mandir}/man1

# Remove hidden files
rm -rf docs/_build/{.buildinfo,.doctrees}

%check
%pyproject_check_import
%pytest

%files -n python3-%{modname} -f %{pyproject_files}
%doc NEWS README.rst

%{_bindir}/mid3cp
%{_bindir}/mid3iconv
%{_bindir}/mid3v2
%{_bindir}/moggsplit
%{_bindir}/mutagen-inspect
%{_bindir}/mutagen-pony

%{_mandir}/man1/mid3cp.1*
%{_mandir}/man1/mid3iconv.1*
%{_mandir}/man1/mid3v2.1*
%{_mandir}/man1/moggsplit.1*
%{_mandir}/man1/mutagen-inspect.1*
%{_mandir}/man1/mutagen-pony.1*

%files doc
%doc docs/_build/*

%changelog
%autochangelog
