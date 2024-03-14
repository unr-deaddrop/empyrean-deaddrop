This is a fork of Empyrean that's used in Pygin. The following modifications have been made:
- All components generate dictionary results that are eventually combined to form a DeadDropMessage.
- The injection module has been removed.
- Some "standalone" functionality, such as persistence, has been removed.

Anti-debug and obfuscation have been preserved in an effort to prevent Windows Defender from randomly blowing up Pygin.

The resulting .exe simply executes all available modules, which have been modified to return their results as a Python dictionary, then combines their results with the name of the module as the dictionary key. The result is JSON serialized to disk as empyrean-result.json, which can then be retrieved (and deleted) by Pygin.

Naturally, this remains Windows-only. When executed on a Linux device, it simply does nothing. It is up to Pygin to refuse to execute the command on identified Linux devices.
