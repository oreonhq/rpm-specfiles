%global source0_hash 484c0206b7cef812b7c00bcba0d3ab4c969452190b10e2a90e9d33d4c7d938dd
%bcond check_jsonschema 0
Name:           bids-schema
Version:        2.0.0
Release:        1%{?dist}
Summary:        BIDS schema description
%global srcversion %(echo '%{version}' | tr '^' '.')
%global bidsversion 1.10.1
License:        CC-BY-4.0
SourceLicense:  CC0-1.0 AND CC-BY-4.0 AND MIT
URL:            https://github.com/bids-standard/bids-specification
Source0:        https://github.com/bids-standard/bids-specification/archive/schema-%{version}/bids-specification-schema-%{version}.tar.gz
%global examples_url https://github.com/bids-standard/bids-examples
%global examples_commit dd545712672537c13ac684b95699b8f11fcedc89
%global error_examples_url https://github.com/bids-standard/bids-error-examples
%global error_examples_commit ac0a2f58f34ce284847dde5bd3b90d7ea048c141
%global examples asl003 ds000248 eeg_cbm micr_SEMzarr micr_SPIM pet003 qmri_tb1tfl
%global error_examples invalid_asl003 invalid_pet001
Source1:        get_test_data
Source2:        bids-examples-%{examples_commit}-filtered.tar.zst
Source3:        bids-error-examples-%{error_examples_commit}-filtered.tar.zst
Source10:       bst.1
Source11:       bst-export.1
Source12:       bst-export-metaschema.1
Source13:       bst-pre-receive-hook.1
BuildArch:      noarch
%if %{with check_jsonschema}
%endif
# oreon:deps
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python3-devel
Requires:       python3-bids-schema = %{version}-%{release}
# /oreon:deps
%description
Portions of the BIDS specification are defined using YAML files in order to
make the specification machine-readable.

Currently the portions of the specification that rely on this schema are:

  • the entity tables,
  • entity definitions,
  • filename templates,
  • metadata tables.

Any changes to the specification should be mirrored in the schema.

%package -n python3-bidsschematools
Summary:        Python tools for working with the BIDS schema
License:        MIT
Requires:       %{name} = %{version}-%{release}
%description -n python3-bidsschematools
A Python library (available after installation in the Python interpreter as
bidsschematools) for working with the Brain Imaging Data Structure (BIDS)
schema.

Features: 

  • lightweight
  • reference schema parsing implementation used for schema testing
  • simple CLI bindings (e.g. bst export)

%prep

test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -n bids-specification-schema-%{srcversion}
%setup -q -T -D -a 2 -c -n bids-specification-schema-%{srcversion}
%setup -q -T -D -a 3 -c -n bids-specification-schema-%{srcversion}

# Remove JavaScript sources used for building the specification documents
# (which we don’t do anyway); these include a bundled pre-compiled/minified
# version of JQuery, which is (license-wise) allowable in the source RPM, but
# must not be shipped in the binary RPMs. Removing it confirms that it is not
# used or shipped. We also preemptively remove the CSS sources, which currently
# don’t contain anything bundled or pre-minified, but are unused and might
# contain something objectionable in a future release.
rm -rf src/js/ src/css/

%build

pushd tools/schemacode >/dev/null
%pyproject_wheel
popd
%install
install -d '%{buildroot}%{_datadir}/bids-schema/versions/%{bidsversion}'
ln -s '%{bidsversion}' '%{buildroot}%{_datadir}/bids-schema/versions/latest'
cp -rvp src/schema \
    '%{buildroot}%{_datadir}/bids-schema/versions/%{bidsversion}/schema'
install -t '%{buildroot}%{_datadir}/bids-schema/versions/%{bidsversion}' \
    -p -m 0644 src/metaschema.json
pushd tools/schemacode >/dev/null
%pyproject_install
popd
install -p -m 0644 \
    -t '%{buildroot}%{_datadir}/bids-schema/versions/%{bidsversion}' \
    '%{buildroot}%{python3_sitelib}/bidsschematools/data/schema.json'
sed -r -i '/\/bidsschematools\/data\/schema(\/|$)/d' %{pyproject_files}
for thing in metaschema.json schema.json
do
  rm "%{buildroot}%{python3_sitelib}/bidsschematools/data/${thing}"
  ln -s \
      "%{buildroot}%{_datadir}/bids-schema/versions/%{bidsversion}/${thing}" \
      "%{buildroot}%{python3_sitelib}/bidsschematools/data/${thing}"
  symlinks -c -o "%{buildroot}%{python3_sitelib}/bidsschematools/data/${thing}"
done
sed -r -i '/\/bidsschematools\/tests(\/|$)/d' %{pyproject_files}
sed -r -i '/bidsschematools\.tests(\.|$)/d' '%{_pyproject_modules}'
rm -rvf '%{buildroot}%{python3_sitelib}/bidsschematools/tests'
install -t '%{buildroot}%{_mandir}/man1' -D -p -m 0644 \
    '%{SOURCE10}' '%{SOURCE11}' '%{SOURCE12}' '%{SOURCE13}'
install -t '%{buildroot}%{_pkgdocdir}' -D -p -m 0644 \
    CITATION.cff
ln -s \
    '%{buildroot}%{_datadir}/bids-schema/versions/%{bidsversion}/schema/README.md' \
    '%{buildroot}%{_pkgdocdir}/README.md'
symlinks -c -o '%{buildroot}%{_pkgdocdir}/README.md'
install -t '%{buildroot}%{_docdir}/python3-bidsschematools' -D -p -m 0644 \
    tools/schemacode/README.md
%oreon_autofiles python3-bidsschematools usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*
%oreon_autofiles main usr/bin/* usr/sbin/* usr/share/man/* usr/share/applications/*

%check

verfile='%{_datadir}/bids-schema/versions/%{bidsversion}/schema/SCHEMA_VERSION'
[ '%{srcversion}' = "$(cat "%{buildroot}${verfile}")" ]
%pyproject_check_import
k="${k-}${k+ and }not test_bids_datasets[hcp_example_bids]"
k="${k-}${k+ and }not test_bids_datasets[qmri_vfa]"
k="${k-}${k+ and }not test_bids_datasets[fnirs_automaticity]"
ln -s "${PWD}/bids-examples-%{examples_commit}" \
    tools/schemacode/tests/data/bids-examples
ln -s "${PWD}/bids-error-examples-%{error_examples_commit}" \
    tools/schemacode/tests/data/bids-error-examples
%if %{without check_jsonschema}
k="${k-}${k+ and }not test_valid_schema_with_check_jsonschema"
%endif
%pytest ${ignore-} -k "${k-}" -v
%files
%files -n python3-bidsschematools -f %{oreon_filedir}/python3-bidsschematools.list

%changelog

%autochangelog
