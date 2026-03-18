# NOTE: ansible-core is in rhel-8.6 and newer, but not installable
# in buildroot as it depended on modular Python.
# It has been installable at buildtime in 8.8 and newer.
%if 0%{?fedora}
BuildRequires: ansible-packaging
%else
%if 0%{?rhel} >= 8
BuildRequires: ansible-core >= 2.11.0
%endif
%endif

%bcond_with collection_artifact

Name: ansible-collection-microsoft-sql
Url: https://github.com/linux-system-roles/mssql
Summary: The Ansible collection for Microsoft SQL Server management
Version: 2.6.4
Release: 3%{?dist}

License: MIT

%global rolename mssql
%global collection_namespace microsoft
%global collection_name sql
%global collection_rolename server
%global collection_version %{version}
%global legacy_rolename %{collection_namespace}.sql-server
%global _pkglicensedir %{_licensedir}/%{name}

# be compatible with the usual Fedora Provides:
Provides: ansible-collection-%{collection_namespace}-%{collection_name} = %{collection_version}-%{release}

# ansible-core is in rhel 8.6 and later - default to ansible-core, but allow
# the use of ansible if present - we may revisit this if the automatic dependency
# generator is added to ansible-core in RHEL
# Fedora - the automatic generator will add this - no need to explicit declare
# it in the spec file
# EL7 - no dependency on ansible because there is no ansible in el7 - user is
# responsible for knowing they have to install ansible
%if 0%{?rhel} >= 8
Requires: (ansible-core >= 2.11.0 or ansible >= 2.9.0)
%endif

%if 0%{?rhel}
Requires: rhel-system-roles
%else
Requires: linux-system-roles
%endif

%global mainid eadd06cfa98d244b096cff24cd11b668428b1613
# Use either hash or tag for source1id
# %%global source1id 50edba099ab2c8b25b225fe760cb5a459b320030
%global source1id %{version}
%global parenturl https://github.com/linux-system-roles
Source: %{parenturl}/auto-maintenance/archive/%{mainid}/auto-maintenance-%{mainid}.tar.gz
Source1: %{parenturl}/%{rolename}/archive/%{source1id}/%{rolename}-%{source1id}.tar.gz

# EL only, includes macros available from ansible-packaging that is not available on EL
Source1002: ansible-packaging.inc
%include %{SOURCE1002}

BuildArch: noarch
# there is no ansible on i686, so when we get a builder that uses
# this arch, the build fails with
# No matching package to install: 'ansible-core >= 2.11.0'
ExcludeArch: i686

# Requirements for galaxy_transform.py
BuildRequires: python3
BuildRequires: python%{python3_pkgversion}-ruamel-yaml

%description
This RPM installs the %{collection_namespace}.%{collection_name} Ansible
collection that provides the %{collection_rolename} role for Microsoft SQL
Server management. This RPM also installs the %{legacy_rolename} role
in the legacy roles format for users of Ansible < 2.9.

%if %{with collection_artifact}
%package collection-artifact
Summary: Collection artifact to import to Automation Hub / Ansible Galaxy

%description collection-artifact
Collection artifact for %{name}. This package contains
%{collection_namespace}-%{collection_name}-%{collection_version}.tar.gz
%endif

%pretrans -p <lua>
path = "%{ansible_roles_dir}/%{legacy_rolename}"
st = posix.stat(path)
if st and st.type == "link" then
  os.remove(path)
end

%prep
%setup -q -a1 -n auto-maintenance-%{mainid}

mv %{rolename}-%{source1id} %{rolename}

# Remove symlinks in tests/roles
if [ -d %{rolename}/tests/roles ]; then
    find %{rolename}/tests/roles -type l -exec rm {} \;
    if [ -d %{rolename}/tests/roles/linux-system-roles.%{rolename} ]; then
        rm -r %{rolename}/tests/roles/linux-system-roles.%{rolename}
    fi
fi

%build
# Move a hidden .README.html to a not hidden README.html
mv %{rolename}/.README.html %{rolename}/README.html

mkdir .collections

# Copy galaxy.yml for the collection build
cp %{rolename}/.collection/galaxy.yml ./

%if 0%{?rhel}
# Ensure the correct entries in galaxy.yml
./galaxy_transform.py "%{collection_namespace}" "%{collection_name}" "%{collection_version}" \
                      "Ansible collection for Microsoft SQL Server management" \
                      "https://github.com/linux-system-roles/mssql" \
                      "https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/automating_system_administration_by_using_rhel_system_roles/assembly_configuring-microsoft-sql-server-using-microsoft-sql-server-ansible-role_automating-system-administration-by-using-rhel-system-roles" \
                      "https://access.redhat.com/articles/3050101" \
                      "https://issues.redhat.com/secure/CreateIssueDetails!init.jspa?pid=12332745&summary=Your%20request%20summary&issuetype=1&priority=10200&labels=Partner-Feature-Request&components=12377164" \
                      > galaxy.yml.tmp
%else
./galaxy_transform.py "%{collection_namespace}" "%{collection_name}" "%{collection_version}" \
                      "Ansible collection for Microsoft SQL Server management" \
                      > galaxy.yml.tmp
%endif
mv galaxy.yml.tmp galaxy.yml

%if 0%{?rhel}
# Replace "fedora.linux_system_roles" with "redhat.rhel_system_roles"
# This is for the "roles calling other roles" case
find . -type f -exec \
     sed -e "s/fedora\.linux_system_roles/redhat.rhel_system_roles/g" \
         -i {} \;
%endif

# Convert to the collection format
python3 lsr_role2collection.py --role "%{rolename}" \
    --src-path "%{rolename}" \
    --src-owner linux-system-roles \
    --dest-path .collections \
    --readme %{rolename}/.collection/README.md \
    --namespace %{collection_namespace} \
    --collection %{collection_name} \
    --new-role "%{collection_rolename}" \
    --meta-runtime lsr_role2collection/runtime.yml

# Replace remnants of "linux-system-roles.mssql" with collection FQDN
find .collections/ansible_collections/%{collection_namespace}/%{collection_name}/ -type f -exec \
     sed -e "s/linux-system-roles[.]%{rolename}\\>/%{collection_namespace}.%{collection_name}.%{collection_rolename}/g" \
         -i {} \;

# removing dot files/dirs
rm -r .collections/ansible_collections/%{collection_namespace}/%{collection_name}/.[A-Za-z]*
rm -r .collections/ansible_collections/%{collection_namespace}/%{collection_name}/tests/%{collection_rolename}/.[A-Za-z]*

# Copy CHANGELOG.md from collection role to parent collection dir
cp .collections/ansible_collections/%{collection_namespace}/%{collection_name}/roles/%{collection_rolename}/CHANGELOG.md \
    .collections/ansible_collections/%{collection_namespace}/%{collection_name}

# Copy galaxy.yml to the collection directory
cp -p galaxy.yml .collections/ansible_collections/%{collection_namespace}/%{collection_name}

# Build collection
pushd .collections/ansible_collections/%{collection_namespace}/%{collection_name}/
%ansible_collection_build
popd

%install
mkdir -p %{buildroot}%{ansible_roles_dir}

# Step 1: Install the role in legacy format
# Copy role in legacy format and rename rolename in tests
cp -pR "%{rolename}" "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}"
find %{buildroot}%{ansible_roles_dir}/%{legacy_rolename} -type f -exec \
     sed -e "s/%{collection_namespace}\.%{collection_name}\.%{collection_rolename}/%{legacy_rolename}/g" \
         -i {} \;

# Copy README, COPYING, CHANGELOG and LICENSE files to the corresponding directories
mkdir -p %{buildroot}%{_pkglicensedir}
mkdir -p "%{buildroot}%{_pkgdocdir}/%{legacy_rolename}"
ln -sr "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/README.md" \
    "%{buildroot}%{_pkgdocdir}/%{legacy_rolename}"
ln -sr "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/README.html" \
    "%{buildroot}%{_pkgdocdir}/%{legacy_rolename}"
ln -sr "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/CHANGELOG.md" \
    "%{buildroot}%{_pkgdocdir}/%{legacy_rolename}"
if [ -f "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/COPYING" ]; then
    ln -sr "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/COPYING" \
        "%{buildroot}%{_pkglicensedir}/%{legacy_rolename}.COPYING"
fi
if [ -f "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/LICENSE" ]; then
    ln -sr "%{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/LICENSE" \
        "%{buildroot}%{_pkglicensedir}/%{legacy_rolename}.LICENSE"
fi

# Remove dot files
rm -r %{buildroot}%{ansible_roles_dir}/*/.[A-Za-z]*
rm -r %{buildroot}%{ansible_roles_dir}/%{legacy_rolename}/tests/.[A-Za-z]*

# Step 2: Remove molecule directory from all roles under ansible_roles_dir
rm -r %{buildroot}%{ansible_roles_dir}/*/molecule

# Step 3: Install the role in collection format
pushd .collections/ansible_collections/%{collection_namespace}/%{collection_name}/
%ansible_collection_install
popd

mkdir -p %{buildroot}%{_pkgdocdir}/collection/roles

# Link collection README to /usr/share/doc/ansible-collection-microsoft-sql/collection.
ln -sr %{buildroot}%{ansible_collection_files}%{collection_name}/README.md \
   %{buildroot}%{_pkgdocdir}/collection

# Link role READMEs to /usr/share/doc/ansible-collection-microsoft-sql/collection/roles/server
mkdir -p %{buildroot}%{_pkgdocdir}/collection/roles/%{collection_rolename}
ln -sr %{buildroot}%{ansible_collection_files}%{collection_name}/roles/%{collection_rolename}/README.md \
    %{buildroot}%{_pkgdocdir}/collection/roles/%{collection_rolename}
ln -sr %{buildroot}%{ansible_collection_files}%{collection_name}/roles/%{collection_rolename}/README.html \
    %{buildroot}%{_pkgdocdir}/collection/roles/%{collection_rolename}

# Link role CHANGELOG.md to /usr/share/doc/ansible-collection-microsoft-sql/collection/roles/server
ln -sr %{buildroot}%{ansible_collection_files}%{collection_name}/roles/%{collection_rolename}/CHANGELOG.md \
    %{buildroot}%{_pkgdocdir}/collection/roles/%{collection_rolename}

# Step 4: Copy collection artifact to /usr/share/ansible/collections/ for collection-artifact
%if %{with collection_artifact}
pushd .collections/ansible_collections/%{collection_namespace}/%{collection_name}/
if [ -f %{collection_namespace}-%{collection_name}-%{collection_version}.tar.gz ]; then
    mv %{collection_namespace}-%{collection_name}-%{collection_version}.tar.gz \
       %{buildroot}%{_datadir}/ansible/collections/
fi
popd
%endif

# Step 5: Generate the %%files section in files_section.txt
# Bulk files inclusion is not possible because roles store doc and licence
# files together with other files
format_item_for_files() {
    # $1 is directory or file name in buildroot
    # $2 - if true, and item is a directory, use %%dir
    local item
    local files_item
    item="$1" # full path including buildroot
    files_item=${item##"%{buildroot}"} # path with cut buildroot to be added to %%files
    if [ -L "$item" ]; then
        echo "$files_item"
    elif [ -d "$item" ]; then
        if [[ "$item" == */doc* ]]; then
            echo "%doc $files_item"
        elif [ "${2:-false}" = true ]; then
            echo "%dir $files_item"
        else
            echo "$files_item"
        fi
    elif [[ "$item" == */README.md ]] || [[ "$item" == */README.html ]] || [[ "$item" == */CHANGELOG.md ]]; then
        if [[ "$item" == */private_* ]]; then
            # mark as regular file, not %%doc
            echo "$files_item"
        else
            echo "%doc $files_item"
        fi
    elif [[ "$item" == */COPYING* ]] || [[ "$item" == */LICENSE* ]]; then
        echo "%""%""license" "$files_item"
    else
        echo "$files_item"
    fi
}

files_section=files_section.txt
rm -f $files_section
touch $files_section
# Dynamically generate files section entries for %%{ansible_collection_files}
find %{buildroot}%{ansible_collection_files}%{collection_name} -mindepth 1 -maxdepth 1 | \
    while read item; do
        if [[ "$item" == */roles ]]; then
            format_item_for_files "$item" true >> $files_section
            find "$item" -mindepth 1 -maxdepth 1 | while read roles_dir; do
                format_item_for_files "$roles_dir" true >> $files_section
                find "$roles_dir" -mindepth 1 -maxdepth 1 | while read roles_item; do
                    format_item_for_files "$roles_item" >> $files_section
                done
            done
        else
            format_item_for_files "$item" >> $files_section
        fi
    done

# Dynamically generate files section entries for %%{ansible_roles_dir}
find %{buildroot}%{ansible_roles_dir} -mindepth 1 -maxdepth 1 | \
    while read item; do
        if [ -d "$item" ]; then
            format_item_for_files "$item" true >> $files_section
            find "$item" -mindepth 1 -maxdepth 1 | while read roles_item; do
                format_item_for_files "$roles_item" >> $files_section
            done
        else
            format_item_for_files "$item" >> $files_section
        fi
    done

%files -f files_section.txt
%dir %{_datadir}/ansible
%dir %{ansible_roles_dir}
%dir %{ansible_collection_files}
%dir %{ansible_collection_files}%{collection_name}
%doc %{_pkgdocdir}
%license %{_pkglicensedir}

%if %{with collection_artifact}
%files collection-artifact
%{_datadir}/ansible/collections/%{collection_namespace}-%{collection_name}-%{collection_version}.tar.gz
%endif

%changelog
* Tue Mar 17 2026 Oreon Packaging Team <packaging@oreonhq.com> - 2.6.4-3
- Prepare for Oreon 11 (RP1)
