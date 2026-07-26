%global source0_hash 8185ab639d75a85627ab4649b060ca2f46b65e2ef4f7c33afbaad18bd26274e0

%global modname mailman3_fedmsg_plugin

%{!?python3_pkgversion: %global python3_pkgversion 3}

Name:               mailman3-fedmsg-plugin
Version:            1.0.1
Release:            2%{?dist}
Summary:            Emit fedora messaging messages from mailman3

License:            LGPL-3.0-or-later
URL:                https://github.com/fedora-infra/mailman3-fedmsg-plugin
Source0:            %{pypi_source %modname}

BuildArch:          noarch

BuildRequires:      python%{python3_pkgversion}-devel

Requires:           fedora-messaging
Requires:           python%{python3_pkgversion}-backoff
Requires:           python%{python3_pkgversion}-mailman3-fedmsg-plugin-schemas
Requires:           mailman3
Requires:           python%{python3_pkgversion}-zope-interface

%global _description %{expand:
Publish notifications about mails to the fedmsg bus.

Enable this by adding the following to your mailman.cfg file::

    [archiver.fedmsg]
    # The class implementing the IArchiver interface.
    class: mailman_fedmsg_plugin.Archiver
    enable: yes

You can exclude certain lists from fedmsg publication by
adding them to a 'mailman.excluded_lists' list in /etc/fedmsg.d/::

    config = {
        'mailman.excluded_lists': ['bugzilla', 'commits'],
    }
}

%description %_description

%package -n python3-%name
Summary: %{summary}

%description -n python3-%name %_description

%generate_buildrequires
%pyproject_buildrequires

%prep
test "%{source0_hash}" = "none" || { f="%{SOURCE0}"; test -f "$f" || { echo "oreon: missing Source0 $f" >&2; exit 1; }; h=$(sha256sum "$f" | awk '{print $1}'); test "$h" = "%{source0_hash}" || { echo "oreon: Source0 hash mismatch" >&2; exit 1; }; }

%autosetup -p1 -n %{modname}-%{version}

# Remove bundled egg-info in case it exists
rm -rf %{modname}.egg-info

%build
%pyproject_wheel

%install
%pyproject_install
%pyproject_save_files %{modname}

%check
%pyproject_check_import %{modname}

%files -n python3-%{name} -f %{pyproject_files}
%doc README.md

%changelog
%autochangelog
