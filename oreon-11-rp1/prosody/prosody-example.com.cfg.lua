-- Section for VirtualHost example.com

VirtualHost "example.com"
	enabled = false -- Remove this line to enable this host

	-- Prosody will automatically search for a certificate and key
	-- in /etc/prosody/certs/ unless a path is manually specified
	-- in the config file, see https://prosody.im/doc/certificates
	--ssl = {
	--	key = "/etc/pki/prosody/example.com.key";
	--	certificate = "/etc/pki/prosody/example.com.crt";
	--}

------ Components ------
-- You can specify components to add hosts that provide special services,
-- like multi-user conferences, and transports.
-- For more information on components, see https://prosody.im/doc/components

---Set up a MUC (multi-user chat) room server on conference.example.com:
--Component "conference.example.com" "muc"
--- Store MUC messages in an archive and allow users to access it
--modules_enabled = { "muc_mam" }

-- Set up a SOCKS5 bytestream proxy for server-proxied file transfers:
--Component "proxy.example.com" "proxy65"

---Set up an external component (default component port is 5347)
--
-- External components allow adding various services, such as gateways/
-- transports to other networks like ICQ, MSN and Yahoo. For more info
-- see: https://prosody.im/doc/components#adding_an_external_component
--
--Component "gateway.example.com"
--	component_secret = "password"
