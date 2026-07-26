If your system has SELinux enabled, you must enable the `httpd_enable_cgi`
boolean:

    # setsebool -P httpd_enable_cgi 1

Additionally, the git repositories need to be accessible to cgit.  This is
handled automatically for repositories in the default path, `/var/lib/git`.

If you have created `/var/lib/git` manually or have existing content in that
directory, you may need to run `restorecon` to reset the SELinux context:

    # restorecon -RF /var/lib/git

If your repositories are in a different path, `/srv/git`, for example, you can
set the proper context using `semanage`:

    # semanage fcontext -a -e /var/lib/git /srv/git

This sets the context of `/srv/git` equal to the default context of
`/var/lib/git`.

If you have other confined daemons that need to access the git repositories,
you may want to use `public_content_t` or `public_content_rw_t` instead:

    # semanage fcontext -a -t public_content_t "/srv/git(/.*)?"

Then use `restorecon` to update the contexts:

    # restorecon -RF /srv/git
