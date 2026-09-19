%global source0_hash none

Name:           python-rdflib
Version:        7.6.0
Release:        %autorelease
# Fill in the actual package summary to submit package to Fedora
Summary:        RDFLib is a Python library for working with RDF, a simple yet powerful language for representing information.

# Check if the automatically generated License and its spelling is correct for Fedora
# https://docs.fedoraproject.org/en-US/packaging-guidelines/LicensingGuidelines/
License:        BSD-3-Clause
URL:            https://github.com/RDFLib/rdflib
Source:         %{pypi_source rdflib}

BuildArch:      noarch
BuildRequires:  python3-devel


# Fill in the actual package description to submit package to Fedora
%global _description %{expand:
This is package 'rdflib' generated automatically by pyp2spec.}

Patch:          0001-Fix-py3.14-test-failure-due-to-NotImplemented-change.patch

%description %_description

%package -n     python3-rdflib
Summary:        %{summary}

%description -n python3-rdflib %_description

# For official Fedora packages, review which extras should be actually packaged
# See: https://docs.fedoraproject.org/en-US/packaging-guidelines/Python/#Extras
%pyproject_extras_subpkg -n python3-rdflib berkeleydb,graphdb,html,lxml,networkx,orjson,rdf4j


%prep
%autosetup -p1 -n rdflib-%{version}


%generate_buildrequires
# Keep only those extras which you actually want to package or use during tests
%pyproject_buildrequires -x berkeleydb,graphdb,html,lxml,networkx,orjson,rdf4j


%build
%pyproject_wheel


%install
%pyproject_install
# For official Fedora packages, including files with '*' +auto is not allowed
# Replace it with a list of relevant Python modules/globs and list extra files in %%files
%pyproject_save_files '*' +auto


%check
%_pyproject_check_import_allow_no_modules -t


%files -n python3-rdflib -f %{pyproject_files}
%{_bindir}/csv2rdf
%{_bindir}/rdf2dot
%{_bindir}/rdfgraphisomorphism
%{_bindir}/rdfpipe
%{_bindir}/rdfs2dot
%{_bindir}/sparqlquery

%changelog
%autochangelog
